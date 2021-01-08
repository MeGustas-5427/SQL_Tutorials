#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'
from datetime import datetime, timedelta
import time
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

    def test_partition(self):
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
                # 注意：使用remove移除分区是仅仅移除分区的定义，并不会删除数据和drop PARTITION不一样，
                # 后者会连同数据一起删除。
                # cursor.execute("ALTER TABLE TestTable REMOVE PARTITIONING;")

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

    def test_partition_and_event_and_procedure(self):
        """
        结合定时任务+存储过程的自动分区
        https://116356754.gitbooks.io/collector_ui/content/chapter1.html
        """
        with connection.cursor() as cursor:
            cursor.execute('select TO_DAYS(''DATE(20210104)'');')
            for result in dictfetchall(cursor):
                print(result)

            today = datetime.now().date()
            yesterday = today - timedelta(days=1)
            cursor.execute(
                f"""
                CREATE TABLE TestTable
                (       # 不能使用主键/唯一键字段之外的其他字段分区(page:185页)
                    created DATETIME
                )
                PARTITION BY LIST (to_days(created))(
                    PARTITION p{yesterday.strftime("%Y%m%d")} VALUES IN (to_days('{yesterday.strftime("%Y-%m-%d")}')),
                    PARTITION p{today.strftime("%Y%m%d")} VALUES IN (to_days('{today.strftime("%Y-%m-%d")}'))
                );
            """
            )

            # 存储过程(插入数据+添加分组+删除分组)
            cursor.execute("""
                CREATE PROCEDURE NewProc(In dbname VARCHAR(512), IN tablename VARCHAR(512))
                BEGIN
                INSERT INTO test_db.TestTable VALUES(NOW());
                /* 事务回滚，其实放这里没什么作用，ALTER TABLE是隐式提交，回滚不了的。
                    declare exit handler for sqlexception rollback;
                    start TRANSACTION; */
                
                    SET @_dbname = dbname;
                    SET @_tablename = tablename;
                
                    /* 到系统表查出这个表的最大编号分区，得到分区的日期。在创建分区的时候，名称就以日期格式存放，方便后面维护 */
                    SET @maxpartition = Concat(
                        "SELECT REPLACE(partition_name,'p','') INTO @P_MaxName FROM INFORMATION_SCHEMA.PARTITIONS WHERE TABLE_SCHEMA='",
                        @_dbname, 
                        "' AND table_name='", 
                        @_tablename, 
                        "' ORDER BY partition_ordinal_position DESC LIMIT 1;"
                    );
                    PREPARE stmt2 FROM @maxpartition;  # 预编译
                    EXECUTE stmt2;
                
                /* 判断最大分区的时间段，如果是前半个月的，那么根据情况需要加13,14,15,16天
                   如果是后半个月的，那么直接加15天。 +0 是为了把日期都格式化成YYYYMMDD这样的格式*/
                    IF (DAY(@P_MaxName)<=15) THEN
                       CASE DAY(LAST_DAY(@P_MaxName))
                          WHEN 31 THEN SET @Max_date=DATE(DATE_ADD(@P_MaxName+0,INTERVAL 16 DAY))+0;
                          WHEN 30 THEN SET @Max_date=DATE(DATE_ADD(@P_MaxName+0,INTERVAL 15 DAY))+0;
                          WHEN 29 THEN SET @Max_date=DATE(DATE_ADD(@P_MaxName+0,INTERVAL 14 DAY))+0; 
                          WHEN 28 THEN SET @Max_date=DATE(DATE_ADD(@P_MaxName+0,INTERVAL 13 DAY))+0; 
                       END CASE;
                    ELSE
                       SET @Max_date=DATE(DATE_ADD(@P_MaxName+0, INTERVAL 15 DAY))+0;
                    END IF;
                
                /* 修改表，在最大分区的后面增加一个分区，时间范围加半个月 */
                    SET @s1=CONCAT(
                        'ALTER TABLE ', 
                        @_tablename, 
                        ' ADD PARTITION (PARTITION p', 
                        @Max_date,
                        ' VALUES IN (TO_DAYS(''',
                        DATE(@Max_date),
                        ''')))'  /* cursor.execute('select TO_DAYS(''DATE(20210104)'');') */
                    );
                    PREPARE stmt2 FROM @s1;
                    EXECUTE stmt2;
                    
                    /* 到系统表查出这个表的最小编号分区，得到分区的日期。*/
                    SET @minpartition = Concat(
                        "SELECT partition_name INTO @P_MinName FROM INFORMATION_SCHEMA.PARTITIONS WHERE TABLE_SCHEMA='",
                        @_dbname, 
                        "' AND table_name='", 
                        @_tablename, 
                        "' ORDER BY partition_ordinal_position LIMIT 1;"
                    );
                    PREPARE stmt2 FROM @minpartition;  # 预编译
                    EXECUTE stmt2;

                    SET @s1=CONCAT('ALTER TABLE ', @_tablename, ' DROP PARTITION ', @P_MinName, ';');
                    # f"ALTER TABLE TestTable DROP PARTITION {min_partition};"
                    SELECT @P_MinName;
                    PREPARE stmt2 FROM @s1;
                    EXECUTE stmt2;
                    
                    DEALLOCATE PREPARE stmt2;
                
                /* 提交
                    COMMIT; */
                END;
            """)

            # MYSQL定时任务
            cursor.execute("""
                CREATE EVENT IF NOT EXISTS test_event
                ON SCHEDULE
                EVERY 5 SECOND
                DO
                CALL NewProc(schema(), 'TestTable');
            """)
            time.sleep(4)
            cursor.execute("""
                SELECT 
                PARTITION_NAME, 
                PARTITION_DESCRIPTION AS descr,
                PARTITION_ORDINAL_POSITION AS position
                FROM INFORMATION_SCHEMA.PARTITIONS 
                WHERE (TABLE_SCHEMA=schema()) AND (TABLE_NAME='TestTable');
            """)
            for result in dictfetchall(cursor):
                print(result)

            cursor.execute("SELECT * FROM TestTable;")
            for result in dictfetchall(cursor):
                print(result)