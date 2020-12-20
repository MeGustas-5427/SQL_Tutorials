#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'

import time

from django.test import TestCase
from django.db import connection, transaction

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.


class TestSQL(TestCase):

    """
    深入浅出MySQL(数据库开发、优化与管理维护)
    10.2.10 事件调度器(表: page-152页)
    """

    def test_event(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE EVENT IF NOT EXISTS test_event
                ON SCHEDULE
                EVERY 5 SECOND
                DO
                INSERT INTO test_db.Vendors VALUES(
                    SUBSTR(MD5(RAND()),1,6),
                    'Bears R Us',
                    '123 Main Street',
                    'Bear Town',
                    'MI',
                    '44444', 
                    'USA'
                );
            """)
            print(cursor.fetchone())

            cursor.execute("show events;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(
                    Db='test_db', 
                    Name='test_event', 
                    Definer='root@%', 
                    Time_zone='SYSTEM', 
                    Type='RECURRING', 
                    Execute_at=None, 
                    Interval_value='5', 
                    Interval_field='SECOND', 
                    Starts=datetime.datetime(2020, 12, 20, 15, 55, 14), 
                    Ends=None, 
                    Status='ENABLED', 
                    Originator=1, 
                    character_set_client='utf8mb4', 
                    collation_connection='utf8mb4_general_ci', 
                    Database_Collation='utf8mb4_unicode_ci'
                )
                """

            cursor.execute("""
                SELECT * FROM Vendors;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                任务创建后会立马执行一次
                Result(vend_id='1fd613', vend_name='Bears R Us', vend_address='123 Main Street', vend_city='Bear Town', vend_state='MI', vend_zip='44444', vend_country='USA')
                """

            print("sleep 6秒...")
            time.sleep(6)

            cursor.execute("""
                SELECT * FROM Vendors;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_id='1fd613', vend_name='Bears R Us', vend_address='123 Main Street', vend_city='Bear Town', vend_state='MI', vend_zip='44444', vend_country='USA')
                Result(vend_id='61d6b4', vend_name='Bears R Us', vend_address='123 Main Street', vend_city='Bear Town', vend_state='MI', vend_zip='44444', vend_country='USA')
                """

            # 修改事件: 清空表
            cursor.execute("""
                ALTER EVENT test_event
                DO
                DELETE FROM test_db.Vendors WHERE 1=1;
            """)

            print("sleep 6秒...")
            time.sleep(6)

            cursor.execute("""
                SELECT * FROM Vendors;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """空"""
            cursor.execute("""ALTER EVENT test_event DISABLE;""")  # 禁用定时任务
            cursor.execute("""DROP EVENT test_event;""")  # 删除定时任务

            cursor.execute("show events;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """空"""

            # 其余例子:
            # 2天后开启每天定时清空Vendors表,一年后停止执行:
            """
            CREATE EVENT test_event
            ON SCHEDULE
            every 1 DAY 
            STARTS
            CURRENT_TIMESTAMP + INTERVAL 2 DAY 
            ENDS
            CURRENT_TIMESTAMP + INTERVAL 1 YEAR 
            DO
            TRUNCATE TABLE test_db.Vendors;
            """

            # 每天定时清空Vendors表(只执行一次,任务完成后就终止该事件):
            """
            CREATE EVENT test_event
            ON SCHEDULE
            every 1 DAY 
            ON COMPLETION NOT PRESERVE 
            DO
            TRUNCATE TABLE test_db.Vendors;
            """

            # 10天后清空Vendors表:
            """
            CREATE EVENT test_event
            ON SCHEDULE
            AT 
            CURRENT_TIMESTAMP + INTERVAL 10 DAY
            DO 
            TRUNCATE TABLE test_db.Vendors;
            """

            # 2013年4月5日12点整清空Vendors表:
            """
            CREATE EVENT test_event
            ON SCHEDULE
            AT 
            timestamp '2013-04-05 12:00:00' 
            DO 
            TRUNCATE TABLE test_db.Vendors;
            """