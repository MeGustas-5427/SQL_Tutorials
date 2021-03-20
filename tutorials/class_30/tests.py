#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'
from django.db.models import Subquery
from django.test import TestCase
from django.db import connection

from tutorials.create_sakila.models import Actor
from tutorials.create_sakila.tests import insert_data, delete_data
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.


class TestSQL(TestCase):
    def setUp(self):
        insert_data()

    def test_prefix_index(self):
        """
        前缀索引, 有效缩小索引文件的大小,但缺点是排序和分组操作的时候无法使用前缀索引.
        """
        with connection.cursor() as cursor:
            cursor.execute("create index idx_title on film(title(10));")

    def test_virtual_column_index(self):
        """
        **8.0.13版本已经支持函数索引**
        如果执行以下这条查询语句, 由于无法建立索引, 因此查询会非常缓慢.
            SELECT * FROM payment WHERE round(amount/10)<10;
        因此, 可以用以下步骤实现函数索引
        ps: 外键不支持函数索引, 函数索引中不允许使用子查询、参数、变量、存储函数以及自定义函数
            函数索引支持UNIQUE选项。但是，主键不能包含函数列。主键只能使用存储的计算列.
            函数索引使用虚拟计算列实现，而不是存储计算列。
            SPATIAL 索引和 FULLTEXT 索引不支持函数索引。
        """
        with connection.cursor() as cursor:
            # 例子1, 数字运算的函数索引测试
            cursor.execute(
                """
                create index idx_amount_by_10 on payment((round(amount/10)));
            """
            )
            cursor.execute(
                """
                show index from payment;
            """
            )
            for result in dictfetchall(cursor):
                print(result)
                _ = {
                    "Table": "payment",
                    "Non_unique": 1,
                    "Key_name": "idx_amount_by_10",
                    "Seq_in_index": 1,
                    "Column_name": None,
                    "Collation": "A",
                    "Cardinality": 2,
                    "Sub_part": None,
                    "Packed": None,
                    "Null": "YES",
                    "Index_type": "BTREE",
                    "Comment": "",
                    "Index_comment": "",
                    "Visible": "YES",
                    "Expression": "round((`amount` / 10),0)",
                }

            cursor.execute(
                """
                explain select count(1) from payment where round(amount/10)>1 AND round(amount/10)<50;
            """
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "payment",
                "partitions": None,
                "type": "ALL",  # 数据类型出现隐式转换的时候,不会使用索引,譬如round(amount/10)是浮点型,1是整型
                "possible_keys": "idx_amount_by_10",
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 15890,
                "filtered": 100,
                "Extra": "Using where",
            }

            cursor.execute(
                """
                explain select count(1) from payment where round(amount/10)>1.0 AND round(amount/10)<50.0;
            """
            )
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "payment",
                "partitions": None,
                "type": "range",  # 数据类型相同才会使用索引,譬如round(amount/10)是浮点型,1.0是浮点型
                "possible_keys": "idx_amount_by_10",
                "key": "idx_amount_by_10",
                "key_len": "3",
                "ref": None,
                "rows": 1,
                "filtered": 100.0,
                "Extra": "Using where",
            }

        with connection.cursor() as cursor:
            # 例子2, 字符串的函数索引测试
            cursor.execute(
                """
                create index idx_title_lower on film((lower(title)));
            """
            )

            title = "ACADEMY DINOSAUR".lower()
            cursor.execute(
                f"explain select title from film where lower(title)='{title}';"
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "film",
                "partitions": None,
                "type": "ref",  # 成功使用函数索引
                "possible_keys": "idx_title_lower",
                "key": "idx_title_lower",
                "key_len": "515",
                "ref": "const",
                "rows": 1,
                "filtered": 100.0,
                "Extra": None,
            }

    def test_secondary_index_select_like(self):
        """
        利用二级索引优化以%开头的LIKE查询不能够利用B-Tree索引的问题

        二级索引是指定字段与主键的映射，主键长度越小，普通索引的叶子节点就越小，
        二级索引占用的空间也就越小，所以要避免使用过长的字段作为主键。
        """
        # 没优化
        with connection.cursor() as cursor:
            # 例子1: 正常情况下的查询, 没有使用上二级索引
            cursor.execute(f"explain select * from actor where last_name like '%NI%';")

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "actor",
                "partitions": None,
                "type": "ALL",  # 没有利用到idx_actor_last_name(二级索引)
                "possible_keys": None,
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 200,
                "filtered": 11.11,
                "Extra": "Using where",
            }

        # 优化
        with connection.cursor() as cursor:
            # 1: 根据二级索引是指定字段与主键的映射的规则,只查询主键,就能触发二级索引
            cursor.execute(
                "explain select actor_id from actor where last_name like '%NI%';"
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "actor",
                "partitions": None,
                "type": "index",
                "possible_keys": None,
                "key": "idx_actor_last_name",
                "key_len": "182",
                "ref": None,
                "rows": 200,
                "filtered": 11.11,
                "Extra": "Using where; Using index",
            }

            # 2: 根据1写出子查询的语句
            cursor.execute(
                """
                explain 
                select * 
                from (select actor_id from actor where last_name like '%NI%') AS a,
                actor AS b
                where a.actor_id = b.actor_id;
                """
            )

            for result in dictfetchall(cursor):
                print(result)
            _1 = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "actor",
                "partitions": None,
                "type": "index",  # 1. 首先二级索引查询对应的主键id
                "possible_keys": "PRIMARY",
                "key": "idx_actor_last_name",
                "key_len": "182",
                "ref": None,
                "rows": 200,
                "filtered": 11.11,
                "Extra": "Using where; Using index",
            }
            _2 = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "b",
                "partitions": None,
                "type": "eq_ref",  # 2. 然后利用聚簇索引从对应的主键id查询出数据
                "possible_keys": "PRIMARY",
                "key": "PRIMARY",
                "key_len": "2",
                "ref": "test_db.actor.actor_id",
                "rows": 1,
                "filtered": 100.0,
                "Extra": None,
            }

        # 采用ORM方式使用子查询写法实现优化
        query_set = Actor.objects.filter(last_name__icontains="NI")
        result = Actor.objects.filter(
            actor_id__in=Subquery(query_set.values("actor_id"))
        )
        print(result.query)
        print(result.explain())
        """
        -> Nested loop inner join  (cost=28.03 rows=22)
            -> Filter: (U0.last_name like '%NI%')  (cost=20.25 rows=22)
                -> Index scan on U0 using idx_actor_last_name  (cost=20.25 rows=200)
            -> Single-row index lookup on actor using PRIMARY (actor_id=U0.actor_id)  (cost=0.25 rows=1)
        """

    def test_mrr(self):
        """
        利用MRR优化JOIN操作
        """

        with connection.cursor() as cursor:

            cursor.execute(
                f"desc select * from payment where customer_id between 1 and 200;"
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "payment",
                "partitions": None,
                "type": "ALL",
                "possible_keys": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 16049,
                "filtered": 33.92,
                "Extra": "Using where",  # 没有使用MRR(using MRR)
            }

            # 通过设置mrr和mrr_cost_based这两个优化器参数使用MRR
            cursor.execute("set optimizer_switch='mrr=on,mrr_cost_based=off';")
            # mrr参数控制MRR特性是否打开(默认on);
            # mrr_cost_based控制是否根据优化器的计算成本来觉得使用MRR特性(默认on);
            # 如果希望尽可能使用MRR,可以将此参数设置为off.

            cursor.execute(
                f"desc select * from payment where customer_id between 1 and 200;"
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "payment",
                "partitions": None,
                "type": "range",
                "possible_keys": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key_len": "2",
                "ref": None,
                "rows": 5444,
                "filtered": 100.0,
                "Extra": "Using index condition; Using MRR",  # 成功使用MRR
            }

    def test_bka(self):
        """
        利用BKA结合MRR优化JOIN操作
        """

        with connection.cursor() as cursor:

            # 通过设置mrr和mrr_cost_based这两个优化器参数使用MRR, batched_key_access控制BKA.
            cursor.execute(
                "set optimizer_switch='mrr=on,mrr_cost_based=off,batched_key_access=on';"
            )
            # mrr参数控制MRR特性是否打开(默认on);
            # mrr_cost_based控制是否根据优化器的计算成本来觉得使用MRR特性(默认on);
            # batched_key_access控制BKA特性(默认on);
            # 如果希望尽可能使用MRR,可以将此参数设置为off.

            """
            通过BKA做JOIN,很多情况下可以提高连接的效率,但对JOIN也有条件限制:
                1、连接的列要求是唯一索引或者普通索引,但不能是主键!
                2、要有对非主键列的查询操作,否则优化器就可以通过覆盖索引等方式
                  直接得到需要的数据,不需要回表,也不需要用到MRR接口.
            由于以上条件苛刻,练习表没有具备演示的足够条件.
            """

    def test_optimize_subqueries(self):
        """
        子查询虽然方便,但采用主键联结并有索引查询会比子查询快
        """
        # 例子1: 从客户表customer中找到不再支付表payment中的所有客户信息:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                explain 
                select * 
                from customer 
                where customer_id not in (select customer_id from payment);
                """
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "customer",
                "partitions": None,
                "type": "ALL",
                "possible_keys": None,
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 599,
                "filtered": 100.0,
                "Extra": None,
            }
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "payment",
                "partitions": None,
                "type": "ref",
                "possible_keys": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key_len": "2",
                "ref": "test_db.customer.customer_id",
                "rows": 1,
                "filtered": 100.0,
                "Extra": "Using where; Not exists; Using index",
            }

            # 优化例子1,采用JOIN查询,因为payment表中堆customer_id建有所有,性能将会更好.
            # JOIN效率更高,是因为MySQL不需要在内存中创建临时表来完成这个逻辑需要两个步骤的查询工作.
            cursor.execute(
                """
                explain 
                select * 
                from customer as a 
                left join payment as b
                on a.customer_id = b.customer_id
                where b.customer_id is null;
                """
            )

            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "a",
                "partitions": None,
                "type": "ALL",
                "possible_keys": None,
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 599,
                "filtered": 100.0,
                "Extra": None,
            }
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "b",
                "partitions": None,
                "type": "ref",  # 查询关联的类型从index_subquery调整为ref,在5.5版本之前,子查询效率不如JOIN
                "possible_keys": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                "key_len": "2",
                "ref": "test_db.a.customer_id",
                "rows": 1,
                "filtered": 100.0,
                "Extra": "Using where; Not exists",
            }

    def test_optimize_or(self):
        """
        优化OR条件查询
            对于含有OR的查询子句,如果要利用索引,则OR之间的每个条件列都必须用到索引;
            如果没有索引,则应该考虑增加索引.
        """
        # 例子1: 当在建有复合索引的列store_id和film_id上面做OR操作,
        #       是不能用到索引idx_store_id_film_id
        with connection.cursor() as cursor:
            cursor.execute(
                """
                explain 
                select * 
                from inventory 
                where store_id<10 or film_id<10;
                """
            )
            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "inventory",
                "partitions": None,
                "type": "ALL",
                "possible_keys": "idx_store_id_film_id,inventory_film_id_609e926a_fk_film_film_id",
                "key": None,
                "key_len": None,
                "ref": None,
                "rows": 4581,
                "filtered": 55.55,
                "Extra": "Using where",
            }

        # 例子2: 当在建有独立索引的列last_name和customer_id上面做OR操作,
        #       是可以正确地用到索引,MySQL处理含有OR的查询实际是对OR的各个
        #       字段分别查询后的结果进行了UNION操作.
        with connection.cursor() as cursor:
            cursor.execute(
                """
                explain 
                select * 
                from customer 
                where last_name='MORGAN' or customer_id<10;
                """
            )
            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "customer",
                "partitions": None,
                "type": "index_merge",
                "possible_keys": "PRIMARY,idx_last_name",
                "key": "idx_last_name,PRIMARY",
                "key_len": "182,2",
                "ref": None,
                "rows": 10,
                "filtered": 100.0,
                "Extra": "Using union(idx_last_name,PRIMARY); Using where",
            }

    def test_optimize_order_by(self):
        """
        优化分页查询
        有两种思路, 这里只写第一种思路, 第二种思路在247页, 比较麻烦因此不写
        """
        # 例子1, 正常分页查询导致全表扫描
        with connection.cursor() as cursor:
            cursor.execute(
                """
                explain 
                select film_id, description 
                from film
                order by title 
                limit 50, 5;
                """
            )
            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 1,
                "select_type": "SIMPLE",
                "table": "film",
                "partitions": None,
                "type": "ALL", # 全表扫描...
                "possible_keys": None,
                "key": None,   # 根据title排序, 而title字段是有普通索引, 但没能使用到普通索引
                "key_len": None,
                "ref": None,
                "rows": 1000,
                "filtered": 100.0,
                "Extra": "Using filesort",
            }

        # 例子2: 利用子查询, 在索引上完成排序分页的操作,
        #       最后根据主键关联回原表查询锁需要的其他列内容
        with connection.cursor() as cursor:
            cursor.execute(
                """
                explain 
                select a.film_id, a.description 
                from film as a
                inner join (
                    select film_id 
                    from film
                    order by title
                    limit 50, 5
                ) as b on a.film_id=b.film_id;
                """
            )
            for result in dictfetchall(cursor):
                print(result)
            _ = {
                "id": 2,
                "select_type": "DERIVED",
                "table": "film",
                "partitions": None,
                "type": "index",  # 优化后使用索引
                "possible_keys": None,
                "key": "idx_title",  # 根据title排序, 而title字段是有普通索引
                "key_len": "514",
                "ref": None,
                "rows": 55,
                "filtered": 100.0,
                "Extra": "Using index",
            }
