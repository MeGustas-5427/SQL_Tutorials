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
    3.1 数值类型(表: page-39页)
    """

    def test_create_table(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (                #  AUTO_INCREMENT: 自增(自动连续编号功能)
                    id INT ZEROFILL AUTO_INCREMENT PRIMARY KEY,  # 主键默认NOT NULL并且UNIQUE(不许重复)
                    tiny TINYINT ZEROFILL,              # 1byte,使用ZEROFILL设置未无符号最小值0, 最大值255
                    small SMALLINT(5) ZEROFILL,         # 2byte,使用ZEROFILL设置未无符号最小值0, 最大值65535
                    medium MEDIUMINT,                   # 3byte
                    inte INTEGER,                       # 4byte
                    big BIGINT                          # 8byte
                )
                CHARSET=utf8mb4;  # 可以选择性增加指定字符编码, 但一般创建数据库设置了字符编码为utf8mb4的话就不用再设置了.
            """)
            print(cursor.fetchone())

            cursor.execute("""
                INSERT INTO TestTable(
                    tiny, 
                    small, 
                    medium, 
                    inte,
                    big
                )
                VALUES (
                    255,
                    87,
                    -8388608,
                    2147483647,
                    9223372036854775807
                );
            """)

            cursor.execute("""
                SELECT * FROM TestTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)