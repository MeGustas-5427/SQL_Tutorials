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

    # 3.1 排序数据
    def test_sort_data(self):
        """
        子句:
        SQL语句由子句构成,有些子句是必需的,有些则是可选的.一个子句通常由一个关键字加上所提供的数据组成.
        子句的例子有SELECT语句的FROM子句.

        注意: ORDER BY 子句的位置
        在指定一条ORDER BY 子句时,应该保证它是SELECT 语句中最后一条子句.如果它不是最后的子句, 报错

        提示: 通过非选择列进行排序
        通常,ORDER BY 子句中使用的列将是为显示而选择的列.但是,实际上并不是一定要这样,用非见搜的列排序
        数据是完全ok的.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT prod_name FROM Products ORDER BY prod_name;")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_name': '12 inch teddy bear'}
                {'prod_name': '18 inch teddy bear'}
                {'prod_name': '8 inch teddy bear'}
                {'prod_name': 'Bird bean bag toy'}
                {'prod_name': 'Fish bean bag toy'}
                {'prod_name': 'King doll'}
                {'prod_name': 'Queen doll'}
                {'prod_name': 'Rabbit bean bag toy'}
                {'prod_name': 'Raggedy Ann'}
                """

    # 3.2 按多个列排序
    def test_multiple_column_sort_data(self):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
            prod_id, prod_price, prod_name 
            FROM 
            Products 
            ORDER BY 
            prod_price, prod_name;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_id': 'BNBG01', 'prod_price': Decimal('3.49'), 'prod_name': 'Fish bean bag toy'}
                {'prod_id': 'BNBG03', 'prod_price': Decimal('3.49'), 'prod_name': 'Rabbit bean bag toy'}
                {'prod_id': 'RGAN01', 'prod_price': Decimal('4.99'), 'prod_name': 'Raggedy Ann'}
                {'prod_id': 'BR01', 'prod_price': Decimal('5.99'), 'prod_name': '8 inch teddy bear'}
                {'prod_id': 'BR02', 'prod_price': Decimal('8.99'), 'prod_name': '12 inch teddy bear'}
                {'prod_id': 'RYL01', 'prod_price': Decimal('9.49'), 'prod_name': 'King doll'}
                {'prod_id': 'RYL02', 'prod_price': Decimal('9.49'), 'prod_name': 'Queen doll'}
                {'prod_id': 'BR03', 'prod_price': Decimal('11.99'), 'prod_name': '18 inch teddy bear'}
                """

    # 3.3 按列位置排序
    def test_position_sort_data(self):
        """
        按列位置排序, 指的是SELECT清单中指定的选择列的相对位置, 譬如说:
            SELECT prod_name, prod_price, prod_id FROM Products ORDER BY 2, 3;
            ORDER BY 2 表示按SELECT清单的第二个列prod_price进行排序,
            ORDER BY 2, 3 表示先按prod_price进行排序,  再按prod_id进行排序

        提示: 按非选择列排序
        显然, 当根据不出现再SELECT 清单中的列进行排序时,不能采用这项技术.但是,如果有必要,可用
        混搭使用实际列名和相对列位置.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
            prod_name, prod_price, prod_id 
            FROM 
            Products 
            ORDER BY 
            2, 3;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_name': 'Fish bean bag toy', 'prod_price': Decimal('3.49'), 'prod_id': 'BNBG01'}
                {'prod_name': 'Bird bean bag toy', 'prod_price': Decimal('3.49'), 'prod_id': 'BNBG02'}
                {'prod_name': 'Rabbit bean bag toy', 'prod_price': Decimal('3.49'), 'prod_id': 'BNBG03'}
                {'prod_name': 'Raggedy Ann', 'prod_price': Decimal('4.99'), 'prod_id': 'RGAN01'}
                {'prod_name': '8 inch teddy bear', 'prod_price': Decimal('5.99'), 'prod_id': 'BR01'}
                {'prod_name': '12 inch teddy bear', 'prod_price': Decimal('8.99'), 'prod_id': 'BR02'}
                {'prod_name': 'King doll', 'prod_price': Decimal('9.49'), 'prod_id': 'RYL01'}
                {'prod_name': 'Queen doll', 'prod_price': Decimal('9.49'), 'prod_id': 'RYL02'}
                {'prod_name': '18 inch teddy bear', 'prod_price': Decimal('11.99'), 'prod_id': 'BR03'}
                """

    # 3.4 指定排序方向
    def test_sort_data_desc(self):
        """
        如果想再多个列上进行降序排序, 必须对每一列指定DESC关键字
        """
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
            prod_price, prod_name, prod_id 
            FROM 
            Products 
            ORDER BY 
            prod_price
            DESC;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_price': Decimal('11.99'), 'prod_name': '18 inch teddy bear', 'prod_id': 'BR03'}
                {'prod_price': Decimal('9.49'), 'prod_name': 'King doll', 'prod_id': 'RYL01'}
                {'prod_price': Decimal('9.49'), 'prod_name': 'Queen doll', 'prod_id': 'RYL02'}
                {'prod_price': Decimal('8.99'), 'prod_name': '12 inch teddy bear', 'prod_id': 'BR02'}
                {'prod_price': Decimal('5.99'), 'prod_name': '8 inch teddy bear', 'prod_id': 'BR01'}
                {'prod_price': Decimal('4.99'), 'prod_name': 'Raggedy Ann', 'prod_id': 'RGAN01'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Fish bean bag toy', 'prod_id': 'BNBG01'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Bird bean bag toy', 'prod_id': 'BNBG02'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Rabbit bean bag toy', 'prod_id': 'BNBG03'}
                """

            print("=" * 60)

            # 多列排序, 某个列为顺序, 某个列为降序
            cursor.execute("""
            SELECT 
            prod_price, prod_name, prod_id 
            FROM 
            Products 
            ORDER BY 
            prod_price DESC,
            prod_name;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_price': Decimal('11.99'), 'prod_name': '18 inch teddy bear', 'prod_id': 'BR03'}
                {'prod_price': Decimal('9.49'), 'prod_name': 'King doll', 'prod_id': 'RYL01'}
                {'prod_price': Decimal('9.49'), 'prod_name': 'Queen doll', 'prod_id': 'RYL02'}
                {'prod_price': Decimal('8.99'), 'prod_name': '12 inch teddy bear', 'prod_id': 'BR02'}
                {'prod_price': Decimal('5.99'), 'prod_name': '8 inch teddy bear', 'prod_id': 'BR01'}
                {'prod_price': Decimal('4.99'), 'prod_name': 'Raggedy Ann', 'prod_id': 'RGAN01'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Bird bean bag toy', 'prod_id': 'BNBG02'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Fish bean bag toy', 'prod_id': 'BNBG01'}
                {'prod_price': Decimal('3.49'), 'prod_name': 'Rabbit bean bag toy', 'prod_id': 'BNBG03'}
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to retrieve all customer names (cust_name) from the Customers table,
           and display the results sorted from Z to A.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT cust_name FROM Customers ORDER BY 1 DESC ;")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys')
                Result(cust_name='The Toy Store')
                Result(cust_name='Kids Place')
                Result(cust_name='Fun4All')
                Result(cust_name='Fun4All')
                """

    def test_exercise2(self):
        """
        2. Write a SQL statement to retrieve customer id (cust_id) and order number (order_num) from
           the Orders table, and sort the results first by customer id, and then by order date in
           reverse chronological order.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT cust_id, order_num FROM Orders ORDER BY 1, order_date DESC;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000001', order_num=20005)
                Result(cust_id='1000000001', order_num=20009)
                Result(cust_id='1000000003', order_num=20006)
                Result(cust_id='1000000004', order_num=20007)
                Result(cust_id='1000000005', order_num=20008)
                """

    def test_exercise3(self):
        """
        3. Our fictitious store obviously prefers to sell more expensive items, and lots of them.
           Write a SQL statement to display the quantity and price (item_price) from the OrderItems
           table, sorted with the highest quantity and highest price first.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT quantity, item_price FROM OrderItems ORDER BY 1 DESC, 2 DESC;")
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(quantity=250, item_price=Decimal('2.49'))
                Result(quantity=250, item_price=Decimal('2.49'))
                Result(quantity=250, item_price=Decimal('2.49'))
                Result(quantity=100, item_price=Decimal('10.99'))
                Result(quantity=100, item_price=Decimal('5.49'))
                Result(quantity=100, item_price=Decimal('2.99'))
                Result(quantity=100, item_price=Decimal('2.99'))
                Result(quantity=100, item_price=Decimal('2.99'))
                Result(quantity=50, item_price=Decimal('11.49'))
                Result(quantity=50, item_price=Decimal('4.49'))
                Result(quantity=20, item_price=Decimal('5.99'))
                Result(quantity=10, item_price=Decimal('11.99'))
                Result(quantity=10, item_price=Decimal('8.99'))
                Result(quantity=10, item_price=Decimal('3.49'))
                Result(quantity=10, item_price=Decimal('3.49'))
                Result(quantity=10, item_price=Decimal('3.49'))
                Result(quantity=5, item_price=Decimal('11.99'))
                Result(quantity=5, item_price=Decimal('4.99'))
                """

    def test_exercise4(self):
        """
        4. What is wrong with the following SQL statement? (Try to figure it out without running it):
        SELECT vend_name,
        FROM Vendors
        ORDER vend_name DESC;
        """
        pass