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
    深入浅出MySQL(数据库开发、优化与管理维护)
    3.4 JSON类型(表: page-52页)
    """

    def test_set_type(self):

        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (                #  AUTO_INCREMENT: 自增(自动连续编号功能)
                    id INT ZEROFILL AUTO_INCREMENT PRIMARY KEY,  # 主键默认NOT NULL并且UNIQUE(不许重复)
                    dict JSON,   # JSON列不可有默认值
                    list JSON
                )
                CHARSET=utf8mb4;  # 可以选择性增加指定字符编码, 但一般创建数据库设置了字符编码为utf8mb4的话就不用再设置了.
            """)
            print(cursor.fetchone())

            cursor.execute("""
                INSERT INTO TestTable(
                    dict,
                    list
                )
                VALUES (
                    '{"age": 20, "time": "2018-07-14 10:52:00"}',  # 隐式插入
                    '[1, 2, 3]'                                    # 隐私插入 
                ), (
                    json_object("name", "abc"),  # 显示插入
                    json_array(4, 5, 6)          # 显示插入
                );
            """)

            cursor.execute("""
                SELECT * FROM TestTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(id=1, dict='{"age": 20, "time": "2018-07-14 10:52:00"}', list='[1, 2, 3]')
                Result(id=2, dict='{"name": "abc"}', list='[4, 5, 6]')
                """

            # JSON_TYPE 函数看json数据的数据类型
            cursor.execute("""
                SELECT JSON_TYPE(dict) AS Dict, JSON_TYPE(list) AS List 
                FROM TestTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(Dict='OBJECT', List='ARRAY')
                Result(Dict='OBJECT', List='ARRAY')
                """

            # JSON_VALID 函数判断JSON数据是否合法
            cursor.execute("""
                 SELECT 
                 JSON_VALID('null') AS n1, 
                 JSON_VALID('NULL') AS n2,  # json数据类型对大小写敏感 
                 JSON_VALID('false') AS n3, 
                 JSON_VALID('FALSE') AS n4;
             """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(n1=1, n2=0, n3=1, n4=0)
                """