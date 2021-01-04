#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'
import datetime
from typing import List

from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall, dictfetchone


# Create your tests here.

"""
深入浅出MySQL(数据库开发、优化与管理维护)
第14章 MySQL分区(page-185页)
"""
class TestSQL(TestCase):
    def setUp(self) -> None:
        self.check_partitions = """
            SELECT 
            PARTITION_NAME, 
            PARTITION_DESCRIPTION AS descr,
            PARTITION_ORDINAL_POSITION AS position,
            TABLE_ROWS 
            FROM INFORMATION_SCHEMA.PARTITIONS 
            WHERE (TABLE_SCHEMA=schema()) AND (TABLE_NAME='TestTable');
        """

    def test_create_partition(self):
        with connection.cursor() as cursor:

            # 1.创建表并设置分区, 通过查看表状态判断是否为为分区表
            def create_partition(cursor):
                cursor.execute(
                    """
                    CREATE TABLE TestTable
                    (       # 不能使用主键/唯一键字段之外的其他字段分区(page:185页)
                        create_year YEAR DEFAULT '2020'  # DEFAULT:设置默认值
                    )
                    PARTITION BY RANGE (create_year)(
                        PARTITION p0 VALUES LESS THAN (1995),
                        PARTITION p1 VALUES LESS THAN (2005),
                        PARTITION p2 VALUES LESS THAN (2015),
                        PARTITION p3 VALUES LESS THAN (2025)
                    )
                """
                )

                cursor.execute("SHOW TABLE STATUS LIKE '%TestTable%';")
                result = [result for result in dictfetchall(cursor)][0]
                print(result)
                print(result["Create_options"] == "partitioned")  # 判断TestTable是否为分区表
                """
                {
                    "Name": "TestTable",
                    "Engine": "InnoDB",
                    "Version": 10,
                    "Row_format": "Dynamic",
                    "Rows": 0,
                    "Avg_row_length": 0,
                    "Data_length": 65536,
                    "Max_data_length": 0,
                    "Index_length": 0,
                    "Data_free": 0,
                    "Auto_increment": None,
                    "Create_time": datetime.datetime(2021, 1, 4, 12, 4, 15),
                    "Update_time": None,
                    "Check_time": None,
                    "Collation": "utf8mb4_unicode_ci",
                    "Checksum": None,
                    "Create_options": "partitioned",
                    "Comment": "",
                }
                """

            # 2.通过查看表设计看分表结构
            def view_structure(cursor):
                cursor.execute("SHOW CREATE TABLE TestTable")
                result = [result for result in dictfetchall(cursor)][0]
                print(result)
                """
                {
                    "Table": "TestTable",
                    "Create Table": "CREATE TABLE `TestTable` "
                                    "(\n  `create_year` year DEFAULT '2020'\n) "
                                    "ENGINE=InnoDB "
                                    "DEFAULT CHARSET=utf8mb4 "
                                    "COLLATE=utf8mb4_unicode_ci\n/*!50100 "
                                    "PARTITION BY RANGE (`create_year`)\n("
                                    "PARTITION p0 VALUES LESS THAN (1995) ENGINE = InnoDB,\n "
                                    "PARTITION p1 VALUES LESS THAN (2005) ENGINE = InnoDB,\n "
                                    "PARTITION p2 VALUES LESS THAN (2015) ENGINE = InnoDB,\n "
                                    "PARTITION p3 VALUES LESS THAN (2025) ENGINE = InnoDB"
                                    ") */",
                }
                """

            # 3.通过INFORMATION_SCHEMA.PARTITIONS表查看指定分区表中的数据分布
            def view_table_row(self, cursor) -> List[str]:

                cursor.execute("""
                    INSERT INTO TestTable VALUES ("1994"), ("2017");
                """)
                cursor.execute(self.check_partitions)
                partition: list = []  # 收集分区的名称
                for result in dictfetchall(cursor):
                    print(result)
                    partition.append(result["PARTITION_NAME"])
                    """
                    {'PARTITION_NAME': 'p0', 'descr': '1995', 'position': 1, 'TABLE_ROWS': 1}
                    {'PARTITION_NAME': 'p1', 'descr': '2005', 'position': 2, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p2', 'descr': '2015', 'position': 3, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p3', 'descr': '2025', 'position': 4, 'TABLE_ROWS': 1}
                    """
                return partition

            # 4. 删除指定分区(一旦修改分区, 则全部TABLE_ROWS都清零, 重新累计)
            def dorp_partition(self, cursor, partition):

                min_partition: str = min(partition, key=lambda x: x.replace("p", ""))
                cursor.execute(f"ALTER TABLE TestTable DROP PARTITION {min_partition};")
                cursor.execute(self.check_partitions)
                for result in dictfetchall(cursor):
                    print(result)
                    """
                    {'PARTITION_NAME': 'p1', 'descr': '2005', 'position': 1, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p2', 'descr': '2015', 'position': 2, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p3', 'descr': '2025', 'position': 3, 'TABLE_ROWS': 0}
                    """

            # 5. 增加指定分区(一旦修改分区, 则全部TABLE_ROWS都清零, 重新累计)
            def add_partition(self, cursor, partition):

                max_partition: str = max(partition, key=lambda x: x.replace("p", ""))
                next_range = int(max_partition.replace('p', '')) + 1
                next_partition: str = f"p{90}"
                range_fun = lambda x: 10 * x + 1995
                cursor.execute(f"""
                    ALTER TABLE TestTable ADD PARTITION (
                        PARTITION {next_partition} VALUES LESS THAN ({range_fun(next_range)})
                    );
                """)
                cursor.execute(self.check_partitions)
                for result in dictfetchall(cursor):
                    print(result)
                    """
                    {'PARTITION_NAME': 'p1', 'descr': '2005', 'position': 1, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p2', 'descr': '2015', 'position': 2, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p3', 'descr': '2025', 'position': 3, 'TABLE_ROWS': 0}
                    {'PARTITION_NAME': 'p90', 'descr': '2035', 'position': 4, 'TABLE_ROWS': 0}
                    """

            create_partition(cursor)
            view_structure(cursor)
            partition = view_table_row(self, cursor)
            dorp_partition(self, cursor, partition)
            add_partition(self, cursor, partition)