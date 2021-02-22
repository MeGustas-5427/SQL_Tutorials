#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection

from tutorials.create_sakila.tests import insert_data, delete_data
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.


class TestSQL(TestCase):
    def setUp(self):
        insert_data()

    def test_show_query_log(self):
        """
        慢查询日志配置
        默认情况下slow_query_log的值为OFF，表示慢查询日志是禁用的，可以通过设置slow_query_log的值来开启
        使用set global slow_query_log=1开启了慢查询日志只对当前数据库生效，如果MySQL重启后则会失效。如果
        要永久生效，就必须修改配置文件my.cnf（其它系统变量也是如此）。
        如果不是调优需要的话，一般不建议启动该参数，因为开启慢查询日志会或多或少带来一定的性能影响。
        """

        with connection.cursor() as cursor:
            cursor.execute("show variables like '%slow_query_log%';")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Variable_name': 'slow_query_log', 'Value': 'OFF'}
                {'Variable_name': 'slow_query_log_file', 'Value': '/var/lib/mysql/9535a632d1ca-slow.log'}
                """
            cursor.execute("set global slow_query_log=1")
            cursor.execute("show variables like '%slow_query_log%';")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Variable_name': 'slow_query_log', 'Value': 'ON'}
                {'Variable_name': 'slow_query_log_file', 'Value': '/var/lib/mysql/9535a632d1ca-slow.log'}
                """

    def test_show_processlist(self):
        """
        show processlist 是显示用户正在运行的线程，实时地查看SQL语句的执行情况,
        需要注意的是，除了 root 用户能看到所有正在运行的线程外，其他用户都只能看到
        自己正在运行的线程，看不到其它用户正在运行的线程。除非单独个这个用户赋予了
        PROCESS 权限。
        https://zhuanlan.zhihu.com/p/30743094
        """

        with connection.cursor() as cursor:
            cursor.execute("show processlist;")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Id': 60, 'User': 'root', 'Host': '172.20.0.1:57390', 'db': 'test_db', 'Command': 'Query', 'Time': 0, 'State': 'starting', 'Info': 'show processlist'}
                ...
                Id:      就是这个线程的唯一标识，当我们发现这个线程有问题的时候，可以通过
                         kill 命令，加上这个Id值将这个线程杀掉。前面我们说了
                         show processlist 显示的信息时来自
                         information_schema.processlist 表，所以这个Id就是这个表的主键。
                User:    就是指启动这个线程的用户。
                Host:    记录了发送请求的客户端的 IP 和 端口号。通过这些信息在排查问题的时
                         候，我们可以定位到是哪个客户端的哪个进程发送的请求。
                DB:      当前执行的命令是在哪一个数据库上。如果没有指定数据库，则该值为 NULL。
                Command: 是指此刻该线程正在执行的命令。这个很复杂，下面单独解释
                Time:    表示该线程处于当前状态的时间。
                State:   线程的状态，和 Command 对应，下面单独解释。
                Info:    一般记录的是线程执行的语句。默认只显示前100个字符，也就是你看到的语
                         句可能是截断了的，要看全部信息，需要使用 show full processlist
                """

    def test_explain(self):
        """通过EXPLAIN分析低效SQL的执行计划"""
        with connection.cursor() as cursor:
            cursor.execute(
                """
                EXPLAIN
                SELECT SUM(amount)
                FROM customer AS a,
                     payment AS b
                WHERE 1 = 1
                  AND a.customer_id = b.customer_id
                  AND email = 'JANE.BENNETT@sakilacustomer.org';
            """
            )
            # 也可以通过EXPLAIN PARTITIONS命令查看SQL所访问的分区,具体看215页.
            for result in dictfetchall(cursor):
                print(result)
                # 具体说明和例子在《深入浅出MySQL(数据库开发、优化与管理维护)》212页
                # https://www.jianshu.com/p/73f2c8448722
                _ = {
                    "id": 1,
                    "select_type": "SIMPLE",  # 表示SELECT的类型，常见的取值有：
                                              #   类型	        说明
                                              #  SIMPLE	   简单表，不使用表连接或子查询
                                              #  PRIMARY   主查询，即外层的查询
                                              #  UNION	   UNION中的第二个或者后面的查询语句
                                              #  SUBQUERY  子查询中的第一个
                    "table": "a",  # 输出结果集的表（表别名）
                    "partitions": None,  # 分区表命中的分区情况。非分区表该字段为空(null)
                    "type": "ALL",  # 表示MySQL在表中找到所需行的方式，或者叫访问类型。
                                    # 常见访问类型如下，从上到下，性能由差到最好：
                                    # ALL	        全表扫描,MySQL遍历全表来找到匹配行
                                    # index	        索引全扫描,MySQL遍历整个索引来查询匹配行,并不会扫描表
                                    # range	        索引范围扫描,常用于<、<=、>、>=、between等操作(被操作字段要有索引)
                                    # ref	        使用非唯一索引或唯一索引的前缀扫描,返回匹配某个单独值的记录行,具体例子看213页.
                                    # eq_ref	    唯一索引扫描,类似ref，区别在于使用的索引是唯一索引,对于每个索引键值,表中只有一条记录匹配
                                    #               就是多表连接中使用主键primary key或者唯一索引unique index作为关联条件.
                                    # const,system	单表最多有一个匹配行,查询起来非常迅速,所以这个匹配行的其他列的值可以被优化器在当前查询中当
                                    #               作常量来处理,例如根据主键primary key或者唯一索引unique index进行的查询.具体例子看213页.
                                    # NULL	        不用扫描表或索引,直接就能够得到结果
                    "possible_keys": "PRIMARY",  # 表示查询可能使用的索引
                    "key": None,      # 实际使用的索引
                    "key_len": None,  # 使用索引字段的长度
                    "ref": None,      # 使用哪个列或常数与key一起从表中选择行
                    "rows": 599,      # 扫描行的数量
                    "filtered": 10.0,  # 存储引擎返回的数据在server层过滤后，剩下多少满足查询的记录数量的比例(百分比)
                    "Extra": "Using where",  # 执行情况的说明和描述，包含不适合在其他列中显示但是对执行计划非常重要的额外信息
                                             # 最主要的有一下四种：
                                             # Using Index	  表示索引覆盖，不会回表查询
                                             # Using Where	  表示进行了回表查询
                                             # Using Index Condition  表示进行了ICP优化
                                             # Using Flesort  表示MySQL需额外排序操作, 不能通过索引顺序达到排序效果
                }
                _ = {
                    "id": 1,
                    "select_type": "SIMPLE",
                    "table": "b",
                    "partitions": None,
                    "type": "ref",
                    "possible_keys": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                    "key": "payment_customer_id_cfa68abe_fk_customer_customer_id",
                    "key_len": "2",
                    "ref": "test_db.a.customer_id",
                    "rows": 1,
                    "filtered": 100.0,
                    "Extra": None,
                }

    def test_show_profile(self):
        """
        通过show profile分析SQL(MYSQL5.7后建议使用性能视图替代profile)
        具体说明和例子在《深入浅出MySQL(数据库开发、优化与管理维护)》216页
        """
        with connection.cursor() as cursor:
            # 查看当前MYSQL是否支持profile
            cursor.execute("SELECT @@have_profiling;")
            for result in dictfetchall(cursor):
                print(result)
                """{'@@have_profiling': 'YES'}"""

            # 默认profiling是关闭的,可以通过set语句在session级别开启profiling
            cursor.execute("set profiling=1;")

            # 查看是否成功开启
            cursor.execute("SELECT @@profiling;")
            for result in dictfetchall(cursor):
                print(result)
                """{'@@profiling': 1}"""  # 成功开启

            # 通过profile,用户能清楚了解SQL执行的过程
            cursor.execute("SELECT COUNT(*) FROM payment;")
            for result in dictfetchall(cursor):
                print(result)
                """{'COUNT(*)': 16049}"""

            # Query_ID': 2 显示了上面的语句查询耗时.
            cursor.execute("show profiles;")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Query_ID': 1, 'Duration': 0.00013125, 'Query': 'SELECT @@profiling'}
                {'Query_ID': 2, 'Duration': 0.0015745, 'Query': 'SELECT COUNT(*) FROM payment'}
                """

            # 通过下面语句能够看到执行过程中线程的每个状态和消耗的时间,详解看217页.
            cursor.execute("show profile for query 2;")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Status': 'starting', 'Duration': Decimal('0.000044')}
                {'Status': 'checking permissions', 'Duration': Decimal('0.000004')}
                {'Status': 'Opening tables', 'Duration': Decimal('0.000012')}
                {'Status': 'init', 'Duration': Decimal('0.000004')}
                {'Status': 'System lock', 'Duration': Decimal('0.000005')}
                {'Status': 'optimizing', 'Duration': Decimal('0.000003')}
                {'Status': 'statistics', 'Duration': Decimal('0.000011')}
                {'Status': 'preparing', 'Duration': Decimal('0.000013')}
                {'Status': 'executing', 'Duration': Decimal('0.001353')}  # 执行
                {'Status': 'end', 'Duration': Decimal('0.000005')}
                {'Status': 'query end', 'Duration': Decimal('0.000002')}
                {'Status': 'waiting for handler commit', 'Duration': Decimal('0.000005')}
                {'Status': 'closing tables', 'Duration': Decimal('0.000004')}
                {'Status': 'freeing items', 'Duration': Decimal('0.000049')}
                {'Status': 'cleaning up', 'Duration': Decimal('0.000009')}
                """

            # MYSQL支持进一步选择all,cpu,block io,context switch,page fault等明细类型查
            # 看MYSQL在使用什么资源上耗费过高的时间,下面显示executing主要耗费在CPU上,详情看218页
            cursor.execute("show profile cpu for query 2;")
            for result in dictfetchall(cursor):
                print(result)
                """
                {'Status': 'starting',                   'Duration': Decimal('0.000064'), 'CPU_user': Decimal('0.000064'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'checking permissions',       'Duration': Decimal('0.000006'), 'CPU_user': Decimal('0.000006'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'Opening tables',             'Duration': Decimal('0.000019'), 'CPU_user': Decimal('0.000019'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'init',                       'Duration': Decimal('0.000005'), 'CPU_user': Decimal('0.000005'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'System lock',                'Duration': Decimal('0.000007'), 'CPU_user': Decimal('0.000007'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'optimizing',                 'Duration': Decimal('0.000004'), 'CPU_user': Decimal('0.000004'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'statistics',                 'Duration': Decimal('0.000015'), 'CPU_user': Decimal('0.000015'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'preparing',                  'Duration': Decimal('0.000013'), 'CPU_user': Decimal('0.000013'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'executing',                  'Duration': Decimal('0.001277'), 'CPU_user': Decimal('0.001609'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'end',                        'Duration': Decimal('0.000049'), 'CPU_user': Decimal('0.000041'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'query end',                  'Duration': Decimal('0.000004'), 'CPU_user': Decimal('0.000004'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'waiting for handler commit', 'Duration': Decimal('0.000007'), 'CPU_user': Decimal('0.000006'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'closing tables',             'Duration': Decimal('0.000005'), 'CPU_user': Decimal('0.000005'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'freeing items',              'Duration': Decimal('0.000047'), 'CPU_user': Decimal('0.000047'), 'CPU_system': Decimal('0.000000')}
                {'Status': 'cleaning up',                'Duration': Decimal('0.000010'), 'CPU_user': Decimal('0.000012'), 'CPU_system': Decimal('0.000000')}

                """