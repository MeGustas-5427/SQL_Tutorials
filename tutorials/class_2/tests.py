#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'

from collections import namedtuple

from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *

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

    @staticmethod
    def dictfetchall(cursor):
        "从cursor获取所有行数据转换成一个字典"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    @staticmethod
    def namedtuplefetchall(cursor):
        "从cursor获取所有行数据转换成一个namedtuple数据类型"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    # 2.2 检索单个列
    def test_select_single_column(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name FROM Products;")
            for result in self.dictfetchall(cursor): # 读取所有
                print(result)
                """
                {'prod_name': 'Fish bean bag toy'}
                {'prod_name': 'Bird bean bag toy'}
                {'prod_name': 'Rabbit bean bag toy'}
                {'prod_name': '8 inch teddy bear'}
                {'prod_name': '12 inch teddy bear'}
                {'prod_name': '18 inch teddy bear'}
                {'prod_name': 'Raggedy Ann'}
                {'prod_name': 'King doll'}
                {'prod_name': 'Queen doll'}
                """

    # 2.3 检索多个列
    def test_select_multiple_column(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_id, prod_name, prod_price FROM Products;")
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result.prod_id, result.prod_name, result.prod_price)
                """
                print(result)
                Result(prod_id='BNBG01', prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_id='BNBG02', prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_id='BNBG03', prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_id='BR01', prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(prod_id='BR02', prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(prod_id='BR03', prod_name='18 inch teddy bear', prod_price=Decimal('11.99'))
                Result(prod_id='RGAN01', prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                Result(prod_id='RYL01', prod_name='King doll', prod_price=Decimal('9.49'))
                Result(prod_id='RYL02', prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 2.4 检索所有列
    def test_select_all_column(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Products;")
            # 注意: 检索不需要的列通常会降低检索速度和应用程序的性能
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(prod_id='BNBG01', prod_name='Fish bean bag toy', prod_price=Decimal('3.49'), prod_desc='Fish bean bag toy, complete with bean bag worms with which to feed it', vend_id='DLL01')
                Result(prod_id='BNBG02', prod_name='Bird bean bag toy', prod_price=Decimal('3.49'), prod_desc='Bird bean bag toy, eggs are not included', vend_id='DLL01')
                Result(prod_id='BNBG03', prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'), prod_desc='Rabbit bean bag toy, comes with bean bag carrots', vend_id='DLL01')
                Result(prod_id='BR01', prod_name='8 inch teddy bear', prod_price=Decimal('5.99'), prod_desc='8 inch teddy bear, comes with cap and jacket', vend_id='BRS01')
                Result(prod_id='BR02', prod_name='12 inch teddy bear', prod_price=Decimal('8.99'), prod_desc='12 inch teddy bear, comes with cap and jacket', vend_id='BRS01')
                Result(prod_id='BR03', prod_name='18 inch teddy bear', prod_price=Decimal('11.99'), prod_desc='18 inch teddy bear, comes with cap and jacket', vend_id='BRS01')
                Result(prod_id='RGAN01', prod_name='Raggedy Ann', prod_price=Decimal('4.99'), prod_desc='18 inch Raggedy Ann doll', vend_id='DLL01')
                Result(prod_id='RYL01', prod_name='King doll', prod_price=Decimal('9.49'), prod_desc='12 inch king doll with royal garments and crown', vend_id='FNG01')
                Result(prod_id='RYL02', prod_name='Queen doll', prod_price=Decimal('9.49'), prod_desc='12 inch queen doll with royal garments and crown', vend_id='FNG01')
                """

    # 2.5 检索不同的值(去重复)
    def test_select_different_value(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT vend_id FROM Products;")
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(vend_id='BRS01')
                Result(vend_id='DLL01')
                Result(vend_id='FNG01')
                """
        """
        注意: 不能部分使用DISTINCT
        DISTINCT 关键字作用与所有的列, 不仅仅是跟在其后的那一列. 例如, 你指定
        SELECT DISTINCT vend_id, prod_price FROM Products;, 则9行里的
        6行都会呗检索处理, 因为指定的两列组合起来有6个不同的结果. 若想看看究竟有
        什么不同, 可以试一下这样两条语句:
        SELECT DISTINCT vend_id, prod_price FROM Products;
        SELECT vend_id, prod_price FROM Products;
        """

    # 2.6 限制结果(不同数据库有不同的实现, 下面是针对MySQL, MariaDB, PostgreSQL, SQLite实现)
    def test_select_limit(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name FROM Products LIMIT 5;")
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy')
                Result(prod_name='Bird bean bag toy')
                Result(prod_name='Rabbit bean bag toy')
                Result(prod_name='8 inch teddy bear')
                Result(prod_name='12 inch teddy bear')
                """
            print("=" * 60)
            cursor.execute("SELECT prod_name FROM Products LIMIT 5 OFFSET 5;")
            """
            分析:
            LIMIT 5 OFFSET 5 指示MySQL等数据库返回从第5行起的5行数据.
            第一个数字是检索的行数, 第二个数字是指从哪一行开始. 
            
            注意:
            第一个呗检索的行是第0行, 而不是第1行. 因此, LIMIT 1 OFFSET 1 会检索第2行, 而不是1行.
            
            提示:
            MySQL, MariaDB, SQLit 可以把LIMIT 4 OFFSET 3 语句简化为 LIMIT 3,4
            使用这个语法, 逗号之前的值对应OFFSET 3, 逗号之后的值对应LIMIT 4 (相反的!! 要小心)
            """
            for result in self.namedtuplefetchall(cursor): # 这个语句的输出是:
                print(result)
                """
                因为Products表只有9种产品, 所有LIMIT 5 OFFSET 5 只返回了4行数据(因为没有第5行)
                Result(prod_name='18 inch teddy bear')
                Result(prod_name='Raggedy Ann')
                Result(prod_name='King doll')
                Result(prod_name='Queen doll')
                """

    # 课后练习
    def test_exercise(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT cust_id FROM Customers;")
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result)

            print("=" * 60)

            cursor.execute("SELECT DISTINCT prod_id FROM OrderItems;")
            for result in self.namedtuplefetchall(cursor): # 读取所有
                print(result)
