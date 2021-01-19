#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'

from datetime import datetime, timedelta

from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall, dictfetchone


# Create your tests here.


class TestSQL(TestCase):

    def test_partitions(self):
        """
        有索引 与 有索引+有分区 的查询速度比较
        以下有:
            1.创建测试用表代码
            2.存储过程(清除旧分区, 创建分区、添加分区)
            3.存储过程(批量插入测试数据)
            4.在正式MySQL环境测试的过程记录
        """
        start = datetime.strptime("1992-01-01", '%Y-%m-%d').date()
        init_day = start.strftime("%Y%m%d")
        print(init_day, start.strftime("%Y-%m-%d"))
        with connection.cursor() as cursor:
            cursor.execute(
                """select TO_DAYS(DATE_ADD(19920101,INTERVAL 1 DAY))""")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)

            # 创建测试用表
            cursor.execute(f"""
                CREATE TABLE TestTable (
                    name varchar(200) DEFAULT 'partition',
                    joined DATE,
                    INDEX joined_idx (joined)
                );
            """)

            # 存储过程(清除旧分区, 创建分区、添加分区)
            cursor.execute("""
                CREATE PROCEDURE NewProc(
                    IN init_day int,
                    IN days int, 
                    IN total_day int, 
                    In dbname VARCHAR(512), 
                    IN tablename VARCHAR(512)
                )
                /* 
                    init_day: 初始日期, 格式19920101
                    days: 天数,按照天数等比划分分区, 譬如days=14, 则每隔14天划分分区
                    total_day: 总天数,按照总天数的范围内划分分区, 譬如在100天内按照days划分分区
                    dbname: 指定数据库名
                    tablename: 指定数据表名
                */
                BEGIN
                    SET init_day = DATE(DATE_ADD(init_day, INTERVAL days DAY))+0;  # 调整初始日期
                    SET total_day = total_day - days;  # 因调整初始日期而调整总天数
                    SET @_db_table = CONCAT(dbname, '.', tablename);
                    SET @count = 1;

                    # 根据判断清除旧分区
                    SELECT
                    CREATE_OPTIONS INTO @has_partition
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE (TABLE_SCHEMA=dbname) AND (TABLE_NAME=tablename);

                    IF (@has_partition = 'partitioned') THEN
                        SET @s1=CONCAT('ALTER TABLE ', @_db_table, ' REMOVE PARTITIONING;');
                        PREPARE stmt2 FROM @s1;
                        EXECUTE stmt2;
                        DEALLOCATE PREPARE stmt2;                        
                    END IF;

                    # 创建分区
                    SET @s1=CONCAT(
                        'ALTER TABLE ',
                        @_db_table, 
                        ' PARTITION BY RANGE (TO_DAYS(joined))(PARTITION p',
                        init_day, 
                        ' VALUES LESS THAN (TO_DAYS(''',
                        init_day,
                        ''')))'  /* cursor.execute('select TO_DAYS(''DATE(20210104)'');') */
                    );
                    PREPARE stmt2 FROM @s1;
                    EXECUTE stmt2;
                    DEALLOCATE PREPARE stmt2;

                    # 添加分区
                    WHILE @count <= total_day DO
                        IF @count % days = 0 THEN
                            SET @date_ = DATE_ADD(init_day,INTERVAL @count DAY);
                            SET @s1=CONCAT(
                                'ALTER TABLE ',
                                @_db_table,
                                ' ADD PARTITION (PARTITION p',
                                DATE(@date_)+0,
                                ' VALUES LESS THAN (TO_DAYS(''',
                                @date_,
                                ''')))'  /* cursor.execute('select TO_DAYS(''DATE(20210104)'');') */
                            );
                            PREPARE stmt2 FROM @s1;
                            EXECUTE stmt2;
                            DEALLOCATE PREPARE stmt2;
                        END IF;
                        SET @count = @count + 1;
                    END WHILE;

                    # 补充最后的分区(超过范围的分区)
                    SET @s1=CONCAT(
                        'ALTER TABLE ',
                        @_db_table,
                        ' ADD PARTITION (PARTITION pMax VALUES LESS THAN MAXVALUE)'
                    );  
                    PREPARE stmt2 FROM @s1;
                    EXECUTE stmt2;
                    DEALLOCATE PREPARE stmt2;
                END;
            """)

            # 存储过程(批量插入测试数据)
            cursor.execute("""
                CREATE PROCEDURE batch_insert_test(
                    IN init_day int, 
                    IN days int, 
                    IN count int, 
                    IN coefficient int,
                    In dbname VARCHAR(512), 
                    IN tablename VARCHAR(512)
                )
                /* 
                    init_day: 初始日期, 格式19920101
                    days: 总天数
                    count: 每天要生成的数据量基数, 通过days * count * coefficient 生成总数据量
                    coefficient: 系数, 每天要生成的数据量系数
                    dbname: 指定数据库名
                    tablename: 指定数据表名
                */
                BEGIN
                    DECLARE total int DEFAULT days * count;  # 创建的总数据量
                    DECLARE str_tmp VARCHAR(16383);
                    DECLARE db_table VARCHAR(50) default CONCAT(dbname, '.', tablename);

                    SET str_tmp = '';
                    SET @date_ = init_day;
                    SET @today_count = 0;  # 用于自增长, 更新@date_

                    WHILE 0 <= total DO      
                        SET str_tmp = concat(str_tmp, "('张三_", total, "', ", @date_, '),');
                        # SELECT str_tmp;
                        IF total % count = 0 THEN
                            # 去除拼接 INSERT 语句之后，最后多的一个逗号，防止语法错误
                            SET str_tmp = LEFT(str_tmp, CHAR_LENGTH(str_tmp)-1);
                            SET @insert_sql_str = CONCAT('INSERT INTO ', db_table, ' VALUES ', str_tmp);
                            PREPARE insert_sql_str FROM @insert_sql_str;

                            SET @coefficient_ = coefficient;
                            REPEAT  # 循环开始
                                EXECUTE insert_sql_str;
                                COMMIT;
                                SET @coefficient_ = @coefficient_ - 1;
                                UNTIL 1 > @coefficient_ 
                            END REPEAT;  # 循环结束

                            DEALLOCATE PREPARE insert_sql_str;

                            SET str_tmp = '';  # 清空要插入的内容
                            SET @today_count = @today_count + 1;
                            SET @date_ = DATE(DATE_ADD(init_day,INTERVAL @today_count DAY))+0;
                        END IF;
                        SET total = total - 1;
                    END WHILE;

                    # 提交剩余数据
                    IF str_tmp != '' THEN
                        SET str_tmp = LEFT(str_tmp, CHAR_LENGTH(str_tmp)-1);
                        SET @insert_sql_str = CONCAT('INSERT INTO ', db_table, ' VALUES ',str_tmp);
                        PREPARE insert_sql_str FROM @insert_sql_str;
                        EXECUTE insert_sql_str;
                        DEALLOCATE PREPARE insert_sql_str;
                        COMMIT;
                    END IF;
                END
            """)

            # 19920101, 7, 10000
            cursor.execute(f"CALL NewProc({init_day}, 3, 20, schema(), 'TestTable')")

            # 19920101, 10000, 500, 20
            cursor.execute(f"CALL batch_insert_test({init_day}, 5, 740, 14, schema(), 'TestTable')")
            cursor.execute("select COUNT(1) from TestTable")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
            cursor.execute("""
                SELECT
                PARTITION_NAME,
                PARTITION_DESCRIPTION AS descr,
                PARTITION_ORDINAL_POSITION AS position,
                TABLE_ROWS
                FROM INFORMATION_SCHEMA.PARTITIONS
                WHERE (TABLE_SCHEMA=schema()) AND (TABLE_NAME='TestTable');
            """)
            for result in dictfetchall(cursor):
                print(result)

            """
            有索引 与 有索引+有分区 的查询速度比较
            测试1亿条数据的

            1.1 创建约1430个分区, 批量插入100000020数据到有索引+有分区的测试表
                CALL NewProc(19920101, 7, 10000, schema(), 'TestTable')
                CALL batch_insert_test(19920101, 10000, 500, 20, schema(), 'TestTable')

            1.2 将TestTable表数据复制到TestNoPartition
                INSERT INTO TestNoPartition SELECT * FROM TestTable;

            1.3 采用的测试查询语句:
                select *
                from TestTable  # 或 TestNoPartition
                where joined = 19950505
                   or joined = 19960505
                   or joined = 19970505
                   or joined = 19980505
                   or joined = 19990505
                   or joined = 20000505
                   or joined = 20010505
                   or joined = 20020505
                   or joined = 20030505
                   or joined = 20040505
                   or joined = 20050505
                   or joined = 20060505
                   or joined = 20070505
                   or joined = 20080505
                   or joined = 20090505
                   or joined = 20100505
                   or joined = 20110505
                   or joined = 20120505
                   or joined = 20130505
                   or joined = 20140505
                   or joined = 20150505
                   or joined = 20160505
                   or joined = 20170505
                   or joined = 20180505
                   or joined = 20190505
                   or joined = 20200505;

            1.4 查询速度结果(没分区的表比有1430个分区的表快):
                # TestTable(2 s 31 ms)
                [2021-01-08 10:40:52] 250,000 rows retrieved starting from 1 in 2 s 31 ms (execution: 35 ms, fetching: 1 s 996 ms)
                # TestNoPartition(1 s 297 ms)
                [2021-01-08 10:41:13] 250,000 rows retrieved starting from 1 in 1 s 297 ms (execution: 47 ms, fetching: 1 s 250 ms)

            1.5 统计全部数据总量的查询速度结果(速度差距更大):
                # TestTable(1 m 31 s 739 ms)
                information_schema> select count(1) as Partitions_ from sql_tutorials_db.TestTable
                [2021-01-08 10:09:21] 1 row retrieved starting from 1 in 1 m 31 s 739 ms (execution: 1 m 31 s 718 ms, fetching: 21 ms)

                # TestNoPartition(27 s 761 ms) 
                information_schema> select count(1) as NotPartitions from sql_tutorials_db.TestNoPartition
                [2021-01-08 10:06:20] 1 row retrieved starting from 1 in 27 s 761 ms (execution: 27 s 745 ms, fetching: 16 ms)

            初步总结:
                原预计有索引分区的表会比仅有索引的表查询速度更快, 但结果相反.
                可能是分区太多, 每个分区仅有7万多条数据, 也许分区太多本身会降低性能.

            2.1 创建11个分区, 批量插入100000020数据到有索引+有分区的测试表
                CALL NewProc(19920101, 1000, 10000, schema(), 'TestTable')
                CALL batch_insert_test(19920101, 10000, 500, 20, schema(), 'TestTable')

            2.2 将TestTable表数据复制到TestNoPartition
                INSERT INTO TestNoPartition SELECT * FROM TestTable;
                sql_tutorials_db> INSERT INTO TestNoPartition SELECT * FROM TestTable
                [2021-01-08 15:15:12] 100,000,020 rows affected in 16 m 20 s 995 ms

            2.3 采用1.3的测试查询语句

            2.4 查询速度结果(没分区的表跟有11个分区的表一样快):
                # TestTable(1 s 197 ms)
                [2021-01-08 15:46:52] 250,000 rows retrieved starting from 1 in 1 s 197 ms (execution: 27 ms, fetching: 1 s 170 ms)
                # TestNoPartition(1 s 240 ms)
                [2021-01-08 15:46:43] 250,000 rows retrieved starting from 1 in 1 s 240 ms (execution: 32 ms, fetching: 1 s 208 ms)

            2.5 统计全部数据总量的查询速度结果(速度相同):            
                # TestTable(26 s 758 ms)
                information_schema> select count(1) as Partitions_ from sql_tutorials_db.TestTable
                [2021-01-08 15:35:03] 1 row retrieved starting from 1 in 26 s 758 ms (execution: 26 s 733 ms, fetching: 25 ms)

                # TestNoPartition(26 s 49 ms)         
                information_schema> select count(1) as NoPartitions from sql_tutorials_db.TestNoPartition
                [2021-01-08 15:36:40] 1 row retrieved starting from 1 in 26 s 49 ms (execution: 26 s 29 ms, fetching: 20 ms)

            二次总结:
                有索引并划分11个分区的表 比 仅有索引的表 查询速度一样.
            """

