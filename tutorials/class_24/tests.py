#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection, transaction

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.

"""
深入浅出MySQL(数据库开发、优化与管理维护)
3.4 JSON类型(表: page-52页)
"""
class TestSQL(TestCase):

    def setUp(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO JsonTable(
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

    def test_select_json(self):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM JsonTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(id=1, dict='{"age": 20, "time": "2018-07-14 10:52:00"}', list='[1, 2, 3]')
                Result(id=2, dict='{"name": "abc"}', list='[4, 5, 6]')
                """

    # JSON_CONTAINS 函数查询文档(array类型数据)是否包含指定的元素
    def test_json_contains(self):
        """JSON_CONTAINS(target, candidate[,path])"""
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT JSON_CONTAINS(list, '5') AS is5  # 查询内容必须使用字符串类型.
                FROM JsonTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(is5=0)
                Result(is5=1)
                """

            cursor.execute("""
                SELECT JSON_CONTAINS(list, '[6,5]') AS is1and5  # 查询内容必须使用字符串类型.
                FROM JsonTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(is1and5=0)
                Result(is1and5=1)
                """

            cursor.execute("""
                SELECT JSON_CONTAINS(dict, '20', '$.age') AS is20  # path:'$.age', path的使用看76页
                FROM JsonTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(is20=1)
                Result(is20=None)
                """

    # JSON_TYPE 函数看json数据的数据类型
    def test_json_type(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT JSON_TYPE(dict) AS Dict, JSON_TYPE(list) AS List
                FROM JsonTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(Dict='OBJECT', List='ARRAY')
                Result(Dict='OBJECT', List='ARRAY')
                """

    # JSON_VALID 函数判断JSON数据是否合法
    def test_json_valid(self):
        with connection.cursor() as cursor:
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