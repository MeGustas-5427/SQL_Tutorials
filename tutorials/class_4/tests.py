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

    # 4.1 使用WHERE 子句
    def test_where(self):
        """
        在SELECT语句中,数据根据WHERE子句中指定的搜索条件进行过滤.
        WHERE子句在表名(FROM子句)之后给出.

        注意: WHERE子句的位置
            在同时使用ORDER BY和WHERE子句时,应该让ORDER BY位于
            WHERE之后,否则将会产生错误.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name, prod_price FROM Products WHERE prod_price = 3.49;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                """

    # 4.2 WHERE 子句操作符
    def test_where_operator(self):
        """
        并非所有DBMS都支持这些操作符, 需要查看对应的DBMS支持哪些操作符
        操作符	    说明                   操作符	        说明
          =	        等于                     >=	        大于等于
          <>	    不等于                   <=	        小于等于
          !=        不等于                   !<          不小于
          >	        大于                     !>          不大于
          <	        小于                     BETWEEN    	在指定的两个值之间
                                            IS NULL     为NULL值
        """
        pass

    # 4.2.1 检查单个值
    def test_check_single_value(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name, prod_price FROM Products WHERE prod_price < 10;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                Result(prod_name='King doll', prod_price=Decimal('9.49'))
                Result(prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 4.2.2 不匹配检查
    def test_mismatch_check(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name, prod_price FROM Products WHERE vend_id <> 'DLL01';")
            """
            提示: 合适使用引号
                如果仔细观察上述WHERE子句中的条件,会看到有的值括在单引号内,
                而有的值未括起来.单引号用来限定字符串.如果将值与字符串类型的
                列进行比较,就需要限定引号.用来与数值列进行比较的值不用引号.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(prod_name='18 inch teddy bear', prod_price=Decimal('11.99'))
                Result(prod_name='King doll', prod_price=Decimal('9.49'))
                Result(prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 4.2.3 范围值检查
    def test_range_value_check(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;")
            """
            分析:
                使用BETWEEN时,必须指定两个值------所需范围的低端值和高端值.
                这两个值必须用AND关键字分隔.BETWEEN匹配范围中所有的值,包括
                指定的开始值和结束值.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(prod_name='King doll', prod_price=Decimal('9.49'))
                Result(prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 4.2.4 控制检查
    def test_null_value_check(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT cust_name, cust_email FROM Customers WHERE cust_email IS NULL;")
            """
            NULL
                无值 (no value), 它与字段包含0,空字符串或仅仅包含空格不同.
            注意: NULL和非匹配
                通过过滤选择不包含指定值的所有行时,你可能希望返回含NULL值的
                行.但是这做不到.因为NULL比较特殊,所以在进行匹配过滤或非匹配
                过滤时,不会返回这些结果.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Kids Place', cust_email=None)
                Result(cust_name='The Toy Store', cust_email=None)
                """
    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to retrieve the product id (prod_id) and
           name (prod_name) from the Products table, returning only
           products with a price of 9.49.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_id, prod_name FROM Products WHERE prod_price = 9.49;")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(prod_id='RYL01', prod_name='King doll')
                Result(prod_id='RYL02', prod_name='Queen doll')
                """

    def test_exercise2(self):
        """
        2. Write a SQL statement to retrieve the product id (prod_id) and name
           (prod_name) from the Products table, returning only products with a
           price of 9 or more.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_id, prod_name FROM Products WHERE prod_price >= 9.49;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BR03', prod_name='18 inch teddy bear')
                Result(prod_id='RYL01', prod_name='King doll')
                Result(prod_id='RYL02', prod_name='Queen doll')
                """

    def test_exercise3(self):
        """
        3. Now let’s combine Lessons 3 and 4. Write a SQL statement that retrieves
           the unique list of order numbers (order_num) from the OrderItems table
           which contain 100 or more of any item.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT order_num FROM OrderItems WHERE quantity >= 100;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005)
                Result(order_num=20007)
                Result(order_num=20009)
                """

    def test_exercise4(self):
        """
        4. One more. Write a SQL statement which returns the product name (prod_name)
           and price (prod_price) from Products for all products priced between 3 and
           6. Oh, and sort the results by price. (There are multiple solutions to
           this one and we’ll revisit it in the next lesson, but you can solve it
           using what you’ve learned thus far).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
            prod_price, prod_name 
            FROM 
            Products 
            WHERE 
            prod_price 
            BETWEEN 3 AND 6 
            ORDER BY 
            prod_price;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_price=Decimal('3.49'), prod_name='Fish bean bag toy')
                Result(prod_price=Decimal('3.49'), prod_name='Bird bean bag toy')
                Result(prod_price=Decimal('3.49'), prod_name='Rabbit bean bag toy')
                Result(prod_price=Decimal('4.99'), prod_name='Raggedy Ann')
                Result(prod_price=Decimal('5.99'), prod_name='8 inch teddy bear')
                """