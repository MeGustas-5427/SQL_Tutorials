#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall, dictfetchone


# Create your tests here.


class TestSQL(TestCase):
    def setUp(self):
        with connection.cursor() as cursor:
            # Populate Customers table
            cursor.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000001', 'Village Toys', '200 Maple Lane', 'Detroit', 'MI', '44444', 'USA', 'John Smith', 'sales@villagetoys.com');")
            cursor.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000002', 'Kids Place', '333 South Lake Drive', 'Columbus', 'OH', '43333', 'USA', 'Michelle Green');")
            cursor.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000003', 'Fun4All', '1 Sunny Place', 'Muncie', 'IN', '42222', 'USA', 'Jim Jones', 'jjones@fun4all.com');")
            cursor.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000004', 'Fun4All', '829 Riverside Drive', 'Phoenix', 'AZ', '88888', 'USA', 'Denise L. Stephens', 'dstephens@fun4all.com');")
            cursor.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000005', 'The Toy Store', '4545 53rd Street', 'Chicago', 'IL', '54545', 'USA', 'Kim Howard');")

            # Populate Vendors table
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRS01','Bears R Us','123 Main Street','Bear Town','MI','44444', 'USA');")
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRE02','Bear Emporium','500 Park Street','Anytown','OH','44333', 'USA');")
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('DLL01','Doll House Inc.','555 High Street','Dollsville','CA','99999', 'USA');")
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FRB01','Furball Inc.','1000 5th Avenue','New York','NY','11111', 'USA');")
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FNG01','Fun and Games','42 Galaxy Road','London', NULL,'N16 6PS', 'England');")
            cursor.execute("INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('JTS01','Jouets et ours','1 Rue Amusement','Paris', NULL,'45678', 'France');")

            # Populate Products table
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR01', 'BRS01', '8 inch teddy bear', 5.99, '8 inch teddy bear, comes with cap and jacket');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR02', 'BRS01', '12 inch teddy bear', 8.99, '12 inch teddy bear, comes with cap and jacket');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR03', 'BRS01', '18 inch teddy bear', 11.99, '18 inch teddy bear, comes with cap and jacket');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG01', 'DLL01', 'Fish bean bag toy', 3.49, 'Fish bean bag toy, complete with bean bag worms with which to feed it');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG02', 'DLL01', 'Bird bean bag toy', 3.49, 'Bird bean bag toy, eggs are not included');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG03', 'DLL01', 'Rabbit bean bag toy', 3.49, 'Rabbit bean bag toy, comes with bean bag carrots');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RGAN01', 'DLL01', 'Raggedy Ann', 4.99, '18 inch Raggedy Ann doll');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL01', 'FNG01', 'King doll', 9.49, '12 inch king doll with royal garments and crown');")
            cursor.execute("INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL02', 'FNG01', 'Queen doll', 9.49, '12 inch queen doll with royal garments and crown');")

            # Populate Orders table
            cursor.execute("INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20005, '2020-05-01', '1000000001');")
            cursor.execute("INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20006, '2020-01-12', '1000000003');")
            cursor.execute("INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20007, '2020-01-30', '1000000004');")
            cursor.execute("INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20008, '2020-02-03', '1000000005');")
            cursor.execute("INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20009, '2020-02-08', '1000000001');")

            # Populate OrderItems table
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 1, 'BR01', 100, 5.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 2, 'BR03', 100, 10.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 1, 'BR01', 20, 5.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 2, 'BR02', 10, 8.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 3, 'BR03', 10, 11.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 1, 'BR03', 50, 11.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 2, 'BNBG01', 100, 2.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 3, 'BNBG02', 100, 2.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 4, 'BNBG03', 100, 2.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 5, 'RGAN01', 50, 4.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 1, 'RGAN01', 5, 4.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 2, 'BR03', 5, 11.99);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 3, 'BNBG01', 10, 3.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 4, 'BNBG02', 10, 3.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 5, 'BNBG03', 10, 3.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 1, 'BNBG01', 250, 2.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 2, 'BNBG02', 250, 2.49);")
            cursor.execute("INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 3, 'BNBG03', 250, 2.49);")

    def tearDown(self):
        # Clean up run after every test method.
        Customers.objects.all().delete()
        Vendors.objects.all().delete()
        Orders.objects.all().delete()
        OrderItems.objects.all().delete()
        Products.objects.all().delete()

    # 12.2.1 创建存储过程
    def test_create_procedure(self):
        """
            在创建存储过程的时候就会输入分隔符“;”。在这种情况下，CREATE PROCEDURE命令就会
        在存储过程不完整的状态下执行。因为在MySQL监视器中一旦输入了分隔符，不管是什么内容，都
        会先执行分隔符之前的部分。
            在存储过程不完整的状态下执行命令会带来一些麻烦，因此我们需要改变环境设置，在输入了
        最后的END之后再执行CREATE PROCEDURE命令。
            因此，在创建存储过程时，需要事先将分隔符从“;”修改为其他符号，一般使用“//”。
            我们可以使用delimiter命令将分隔符修改为“//”。
            如果将分隔符设置为“//”，那么即使在创建存储过程的途中输入了“;”也不会发生任何问
        题。在END之后输入“//”，这时就会执行CREATE PROCEDURE命令。存储过程创建结束后，使
        用“delimiter ;”将分隔符恢复为原始设置。
        """
        # mysql> delimiter //
        # mysql> CREATE PROCEDURE test_func()
        #     -> BEGIN
        #     -> SELECT * FROM Customers;
        #     -> SELECT * FROM Orders;
        #     -> END
        #     -> //
        # mysql> delimiter ;
        # mysql> CALL test_func;

        # 12.2.3 创建只显示大于等于指定值的记录的存储过程(MySQL基础教程)
        # mysql> delimiter //
        # mysql> CREATE PROCEDURE test_func(count INT)
        #     -> BEGIN
        #     -> SELECT * FROM OrderItems WHERE quantity>=count;
        #     -> END
        #     -> //
        # mysql> delimiter ;
        # mysql> CALL test_func(100);
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE PROCEDURE test_func(count INT)
                BEGIN
                SELECT id, order_item, quantity FROM OrderItems WHERE quantity>count;
                END
            """)
            cursor.execute("CALL test_func(100);")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'id': 16, 'order_item': 1, 'quantity': 250}
                {'id': 17, 'order_item': 2, 'quantity': 250}
                {'id': 18, 'order_item': 3, 'quantity': 250}
                """

            # 12.3.1 显示存储过程的内容(MySQL基础教程)
            # mysql> SHOW CREATE PROCEDURE test_func \G
            cursor.execute("SHOW CREATE PROCEDURE test_func;")
            result = dictfetchone(cursor)  # 读取
            print(result)
            """
            {
                'Procedure': 'test_func', 
                'sql_mode': 'STRICT_TRANS_TABLES', 
                'Create Procedure': 'CREATE DEFINER=`root`@`%` PROCEDURE `test_func`(count INT)\n'
                                    'BEGIN\n                '
                                    'SELECT id, order_item, quantity FROM OrderItems WHERE quantity>count;\n        '
                                    'END', 
                'character_set_client': 'utf8mb4', 
                'collation_connection': 'utf8mb4_general_ci', 
                'Database Collation': 'utf8mb4_unicode_ci'
            }
            """

            # 12.3.2 删除存储过程(MySQL基础教程)
            # mysql> DROP PROCEDURE test_func;
            cursor.execute("DROP PROCEDURE test_func;")


    # 12.5 使用存储函数(MySQL基础教程)
    def test_use_storage_func(self):
        ""
        """
        # log_bin_trust_function_creators的初始值为OFF是不能存储函数, 必须设置为ON.
        # 重启数据库会恢复为OFF,可修改配置文件解决重启问题. 使用存储函数需要权限, root已有权限.

        mysql> SHOW VARIABLES LIKE 'log_bin_trust_function_creators';
        +---------------------------------+-------+
        | Variable_name                   | Value |
        +---------------------------------+-------+
        | log_bin_trust_function_creators | OFF   |
        +---------------------------------+-------+
        1 row in set (0.00 sec)

        mysql> SET GLOBAL log_bin_trust_function_creators=1;
        Query OK, 0 rows affected (0.00 sec)

        mysql> SHOW VARIABLES LIKE 'log_bin_trust_function_creators';
        +---------------------------------+-------+
        | Variable_name                   | Value |
        +---------------------------------+-------+
        | log_bin_trust_function_creators | ON    |
        +---------------------------------+-------+
        1 row in set (0.00 sec)

        mysql> delimiter //
        mysql> CREATE FUNCTION test_func(count INT) RETURNS DOUBLE
            -> BEGIN
            -> RETURN count*22/1000;
            -> END
            -> //
        mysql> delimiter ;        
        mysql> SELECT test_func(345);
        +----------------+
        | test_func(345) |
        +----------------+
        |           7.59 |
        +----------------+
        1 row in set (0.00 sec)
        
        mysql>
        """
        with connection.cursor() as cursor:
            # 12.5.2 使用存储函数计算(MySQL基础教程)
            cursor.execute("""
                CREATE FUNCTION test_func(count INT) RETURNS DOUBLE
                BEGIN
                RETURN count*22/1000;
                END
            """)
            cursor.execute("SELECT test_func(345) AS result;")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                "{'result': 7.59}"

            # 12.5.3 返回记录平均值的存储函数(MySQL基础教程)
            cursor.execute("""
                CREATE FUNCTION order_items_func() RETURNS DOUBLE
                BEGIN
                DECLARE result DOUBLE;  # 定义变量: DECLARE 变量名 数据类型;
                SELECT AVG(quantity) INTO result FROM OrderItems;  # 把平均值通过INTO赋给变量result
                RETURN result;
                END
            """)
            cursor.execute("SELECT order_items_func() AS result;")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                "{'result': 79.444444444}"

            # 12.5.4 显示和删除存储函数
            # 显示存储函数
            cursor.execute("SHOW CREATE FUNCTION order_items_func;")
            result = dictfetchone(cursor)  # 读取
            print(result)
            """
            {
                'Function': 'order_items_func', 
                'sql_mode': 'STRICT_TRANS_TABLES', 
                'Create Function': 'CREATE DEFINER=`root`@`%` FUNCTION `order_items_func`() RETURNS double\n'
                                   'BEGIN\n                '
                                   'DECLARE result DOUBLE;  # 定义变量: DECLARE 变量名 数据类型;\n                '
                                   'SELECT AVG(quantity) INTO result FROM OrderItems;  # 把平均值通过INTO赋给变量result\n'
                                   'RETURN result;\n                '
                                   'END', 
                'character_set_client': 'utf8mb4', 
                'collation_connection': 'utf8mb4_general_ci',
                'Database Collation': 'utf8mb4_unicode_ci'
            }
            """
            # 删除存储函数
            cursor.execute("DROP FUNCTION order_items_func;")