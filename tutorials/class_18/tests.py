#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall


# Create your tests here.


class TestSQL(TestCase):
    def setUp(self):
        with connection.cursor() as cursor:
            # Populate Customers table
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000001', 'Village Toys', '200 Maple Lane', 'Detroit', 'MI', '44444', 'USA', 'John Smith', 'sales@villagetoys.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000002', 'Kids Place', '333 South Lake Drive', 'Columbus', 'OH', '43333', 'USA', 'Michelle Green');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000003', 'Fun4All', '1 Sunny Place', 'Muncie', 'IN', '42222', 'USA', 'Jim Jones', 'jjones@fun4all.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000004', 'Fun4All', '829 Riverside Drive', 'Phoenix', 'AZ', '88888', 'USA', 'Denise L. Stephens', 'dstephens@fun4all.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000005', 'The Toy Store', '4545 53rd Street', 'Chicago', 'IL', '54545', 'USA', 'Kim Howard');"
            )

            # Populate Vendors table
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRS01','Bears R Us','123 Main Street','Bear Town','MI','44444', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRE02','Bear Emporium','500 Park Street','Anytown','OH','44333', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('DLL01','Doll House Inc.','555 High Street','Dollsville','CA','99999', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FRB01','Furball Inc.','1000 5th Avenue','New York','NY','11111', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FNG01','Fun and Games','42 Galaxy Road','London', NULL,'N16 6PS', 'England');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('JTS01','Jouets et ours','1 Rue Amusement','Paris', NULL,'45678', 'France');"
            )

            # Populate Products table
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR01', 'BRS01', '8 inch teddy bear', 5.99, '8 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR02', 'BRS01', '12 inch teddy bear', 8.99, '12 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR03', 'BRS01', '18 inch teddy bear', 11.99, '18 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG01', 'DLL01', 'Fish bean bag toy', 3.49, 'Fish bean bag toy, complete with bean bag worms with which to feed it');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG02', 'DLL01', 'Bird bean bag toy', 3.49, 'Bird bean bag toy, eggs are not included');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG03', 'DLL01', 'Rabbit bean bag toy', 3.49, 'Rabbit bean bag toy, comes with bean bag carrots');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RGAN01', 'DLL01', 'Raggedy Ann', 4.99, '18 inch Raggedy Ann doll');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL01', 'FNG01', 'King doll', 9.49, '12 inch king doll with royal garments and crown');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL02', 'FNG01', 'Queen doll', 9.49, '12 inch queen doll with royal garments and crown');"
            )

            # Populate Orders table
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20005, '2020-05-01', '1000000001');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20006, '2020-01-12', '1000000003');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20007, '2020-01-30', '1000000004');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20008, '2020-02-03', '1000000005');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20009, '2020-02-08', '1000000001');"
            )

            # Populate OrderItems table
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 1, 'BR01', 100, 5.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 2, 'BR03', 100, 10.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 1, 'BR01', 20, 5.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 2, 'BR02', 10, 8.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 3, 'BR03', 10, 11.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 1, 'BR03', 50, 11.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 2, 'BNBG01', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 3, 'BNBG02', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 4, 'BNBG03', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 5, 'RGAN01', 50, 4.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 1, 'RGAN01', 5, 4.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 2, 'BR03', 5, 11.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 3, 'BNBG01', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 4, 'BNBG02', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 5, 'BNBG03', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 1, 'BNBG01', 250, 2.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 2, 'BNBG02', 250, 2.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 3, 'BNBG03', 250, 2.49);"
            )

    def tearDown(self):
        # Clean up run after every test method.
        Customers.objects.all().delete()
        Vendors.objects.all().delete()
        Orders.objects.all().delete()
        OrderItems.objects.all().delete()
        Products.objects.all().delete()

    # 11.4.3 当插入的数据与视图的条件不匹配时报错(MySQL基础教程)
    def test_with_check_option(self):
        with connection.cursor() as cursor:
            # 创建视图
            cursor.execute("""
                CREATE OR REPLACE VIEW VendorLocations AS  # OR REPLACE:删除已存在的同名视图,创建新的视图.
                SELECT *
                FROM Vendors
                WHERE vend_state IN ('CA')
                WITH CHECK OPTION;  # 防止INSERT的数据与WHERE条件不匹配的记录, 造成麻烦的事情.
            """)

            # 11.5.2 修改视图结构(MySQL基础教程)
            cursor.execute("""
                ALTER VIEW VendorLocations AS
                SELECT *
                FROM Customers;
            """)

            # 11.5.3 删除视图(MySQL基础教程)
            cursor.execute("""
                DROP VIEW IF EXISTS VendorLocations;
            """)

    # 18.2.1 利用视图简化复杂得联结
    def test_update_a_value(self):
        with connection.cursor() as cursor:
            # 创建视图
            cursor.execute("""
                CREATE VIEW ProductCustomers AS
                SELECT cust_name, cust_contact, OI.prod_id
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                INNER JOIN OrderItems OI on O.order_num = OI.order_num;
            """)
            # 使用视图检索
            cursor.execute("""
            SELECT cust_name, cust_contact
            FROM ProductCustomers
            WHERE prod_id = 'RGAN01';
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Fun4All', cust_contact='Denise L. Stephens')
                Result(cust_name='The Toy Store', cust_contact='Kim Howard')
                """

    # 18.2.2 用视图重新格式化检索除的数据
    def test_update_multiple_values(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE VIEW VendorLocations AS
                SELECT CONCAT(RTRIM(vend_name), '(', RTRIM(vend_country), ')') AS vend_title
                FROM Vendors;
            """)
            cursor.execute("""
                SELECT * FROM VendorLocations
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_title='Bear Emporium(USA)')
                Result(vend_title='Bears R Us(USA)')
                Result(vend_title='Doll House Inc.(USA)')
                Result(vend_title='Fun and Games(England)')
                Result(vend_title='Furball Inc.(USA)')
                Result(vend_title='Jouets et ours(France)')
                """

    # 18.2.3 用视图过滤不想要的数据
    def test_update_to_null(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE VIEW CustomerEMailList AS
                SELECT cust_id, cust_name, cust_email
                FROM Customers
                WHERE cust_email IS NOT NULL;
            """)
            """
            说明：WHERE子句与WHERE子句
                从视图检索数据时如果使用了一条WHERE子句，则两组子句（一组在 
                视图中，另一组是传递给视图的）将自动组合。
            """
            cursor.execute("""
                SELECT * FROM CustomerEMailList
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000001', cust_name='Village Toys', cust_email='sales@villagetoys.com')
                Result(cust_id='1000000003', cust_name='Fun4All', cust_email='jjones@fun4all.com')
                Result(cust_id='1000000004', cust_name='Fun4All', cust_email='dstephens@fun4all.com')
                """

    # 18.2.4 使用视图与计算字段
    def test_delete_date(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE VIEW OrderItemsExpanded AS
                SELECT order_num, quantity, item_price, quantity*item_price AS expanded_price
                FROM OrderItems;
            """)
            cursor.execute("""
                SELECT *
                FROM OrderItemsExpanded
                WHERE order_num = 20008;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20008, quantity=5, item_price=Decimal('4.99'), expanded_price=Decimal('24.95'))
                Result(order_num=20008, quantity=5, item_price=Decimal('11.99'), expanded_price=Decimal('59.95'))
                Result(order_num=20008, quantity=10, item_price=Decimal('3.49'), expanded_price=Decimal('34.90'))
                Result(order_num=20008, quantity=10, item_price=Decimal('3.49'), expanded_price=Decimal('34.90'))
                Result(order_num=20008, quantity=10, item_price=Decimal('3.49'), expanded_price=Decimal('34.90'))
                """

    # 11.2.2 通过视图更新列的值(MySQL基础教程)
    # 如果更新了视图的值, 基表的值也会随之更新. 因为视图不仅仅是基表的一部分,
    # 它也是指向基表数据的窗口. 相反, 基表的数据更新, 视图对应的数据也会更新.

    # 11.4 限制通过视图写入(MySQL基础教程)
    # 如果再使用了UNION,JOIN,子查询的视图中,不能执行INSERT和UPDATE.
    # 如果只是从一个表中创建的视图,那么执行INSERT和UPDATE是没有任何问题的.

    # 课后练习
    def test_exercise1(self):
        """
        1. Create a view called CustomersWithOrders that contains all of the columns
           in Customers, but only includes those who have placed orders. Hint, you
           can JOIN the Orders table to filter just the customers you want. Then use
           a SELECT to make sure you have the right data.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE VIEW CustomersWithOrders AS
                SELECT Customers.*
                FROM Customers
                RIGHT OUTER JOIN Orders O on Customers.cust_id = O.cust_id;
            """)

            cursor.execute("""
                SELECT * FROM CustomersWithOrders;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)

    def test_exercise2(self):
        """
        2. What is wrong with the following SQL statement? (Try to figure it out
           without running it):
        """
        """
        CREATE VIEW OrderItemsExpanded AS
        SELECT order_num,
               prod_id,
               quantity,
               item_price,
               quantity*item_price AS expanded_price
        FROM OrderItems
        ORDER BY order_num;
        """
