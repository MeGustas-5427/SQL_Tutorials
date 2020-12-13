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
    3.3 字符串类型类型(表: page-49页)
    """

    def test_set_type(self):
        """
        SET和ENUM类似, 都是一个字符串对象, 最主要的区别在于SET类型一次可以选取多个成员,
        而ENUM则只能选一个.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (                #  AUTO_INCREMENT: 自增(自动连续编号功能)
                    id INT ZEROFILL AUTO_INCREMENT PRIMARY KEY,  # 主键默认NOT NULL并且UNIQUE(不许重复)
                    col SET ("a", "b", "c", "d")   # 1~8成员的集合, 占1个byte, 更多成员所占的byte看书52页
                )
                CHARSET=utf8mb4;  # 可以选择性增加指定字符编码, 但一般创建数据库设置了字符编码为utf8mb4的话就不用再设置了.
            """)
            print(cursor.fetchone())

            cursor.execute("""
                INSERT INTO TestTable(
                    col
                )
                VALUES (
                    "a,b"
                ), (
                    "c,d,a"
                ), (
                    "d,a"
                );
            """)

            cursor.execute("""
                SELECT * FROM TestTable;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(id=1, col='a,b')
                Result(id=2, col='a,c,d')
                Result(id=3, col='a,d')
                """