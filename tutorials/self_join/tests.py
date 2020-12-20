#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection, transaction

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.


class TestSQL(TestCase):

    """
    SQL优化大神带你写有趣的SQL(6) SELF JOIN的应用
    https://mp.weixin.qq.com/s/InboZo8JkZyHDeswAiopvQ
    """

    def test_self_join(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                create table t0718 (
                    idx int,
                    no int ,
                    val1 varchar(30),
                    val2 varchar(10)
                )
                CHARSET=utf8mb4;  # 可以选择性增加指定字符编码, 但一般创建数据库设置了字符编码为utf8mb4的话就不用再设置了.
            """)
            print(cursor.fetchone())

            cursor.execute("""
                insert into t0718 values( 1 ,10 ,'1 2 3' ,'11');
                insert into t0718 values( 2 ,20 ,'4 5 6' ,'12');
                insert into t0718 values( 3 ,30 ,'7 8 9' ,'13');
                insert into t0718 values( 4 ,40 ,'4 8 9' ,'14');
                insert into t0718 values( 5 ,50 ,'1 4 8' ,'15');
                insert into t0718 values( 6 ,55 ,'3 2 9' ,'21');
                insert into t0718 values( 7 ,13 ,'7 0 4' ,'33');
                insert into t0718 values( 8 ,77 ,'1 6 9' ,'45');
                insert into t0718 values( 9 ,22 ,'5 7 8' ,'23');
                insert into t0718 values( 10 ,77 ,'8 0 9' ,'99');
            """)
            """
            | idx | no | val1  | val2 |
            | 1   | 10 | 1 2 3 |  11  | 
            | 2   | 20 | 4 5 6 |  12  | 
            | 3   | 30 | 7 8 9 |  13  | 
            | 4   | 40 | 4 8 9 |  14  | 
            | 5   | 50 | 1 4 8 |  15  | 
            | 6   | 55 | 3 2 9 |  21  | 
            | 7   | 13 | 7 0 4 |  33  | 
            | 8   | 77 | 1 6 9 |  45  | 
            | 9   | 22 | 5 7 8 |  23  | 
            | 10  | 77 | 8 0 9 |  99  | 
            
            在如上的数据中，对val1 进行查询，如果查到了，如输入值为2 ，
            那就返回，从下一行开始的三行数据，返回结果如下:
            
            | idx | no | val1  | val2 |
            | 2   | 20 | 4 5 6 |  12  | 
            | 3   | 30 | 7 8 9 |  13  | 
            | 4   | 40 | 4 8 9 |  14  | 
            | 7   | 13 | 7 0 4 |  33  | 
            | 8   | 77 | 1 6 9 |  45  | 
            | 9   | 22 | 5 7 8 |  23  | 
            """
            # 中间过程:
            cursor.execute("""
                SELECT t.* from t0718 as t, t0718 as t1
                WHERE (t1.val1 like '%2%')
                AND (t1.idx < t.idx);
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(idx=2, no=20, val1='4 5 6', val2='12')
                Result(idx=3, no=30, val1='7 8 9', val2='13')
                Result(idx=4, no=40, val1='4 8 9', val2='14')
                Result(idx=5, no=50, val1='1 4 8', val2='15')
                Result(idx=6, no=55, val1='3 2 9', val2='21')
                Result(idx=7, no=13, val1='7 0 4', val2='33')
                Result(idx=8, no=77, val1='1 6 9', val2='45')
                Result(idx=9, no=22, val1='5 7 8', val2='23')
                Result(idx=10, no=77, val1='8 0 9', val2='99')
                
                Result(idx=7, no=13, val1='7 0 4', val2='33')
                Result(idx=8, no=77, val1='1 6 9', val2='45')
                Result(idx=9, no=22, val1='5 7 8', val2='23')
                Result(idx=10, no=77, val1='8 0 9', val2='99')
                """
            print("="*60)
            # 最终查询语句:
            cursor.execute("""
                SELECT t.* from t0718 as t, t0718 as t1
                WHERE (t1.val1 like '%2%')
                AND (t1.idx < t.idx)
                AND (t1.idx+3 >= t.idx);
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(idx=2, no=20, val1='4 5 6', val2='12')
                Result(idx=3, no=30, val1='7 8 9', val2='13')
                Result(idx=4, no=40, val1='4 8 9', val2='14')
                Result(idx=7, no=13, val1='7 0 4', val2='33')
                Result(idx=8, no=77, val1='1 6 9', val2='45')
                Result(idx=9, no=22, val1='5 7 8', val2='23')
                """