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

    # 9.1 聚集(聚合)函数
    """
    AVG()     返回某列的平均值
    COUNT()   返回某列的行数
    MAX()     返回某列的最大值
    MIN()     返回某列的最小值
    SUM()     返回某列之和
    """

    # 9.1.1 AVG()函数
    def test_avg_func(self):
        """
        说明:
            AVG()函数忽略列值为NULL的行.

        注意: 只用于单个列
            AVG()只能用来确定特定数值列的平均值,而且列名必须作为函数参数
            给出.为了获得多个列的平均值,必须使用多个AVG()函数.只有一个例
            外是要从多个列计算出一个值. 下面会说.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT AVG(prod_price) AS avg_price 
                FROM Products;
                """)
            """
            AVG(): 返回某列的平均值
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'avg_price': Decimal('6.823333')}
                """

            print("=" * 60)

            cursor.execute("""
                SELECT AVG(prod_price) AS avg_price 
                FROM Products
                WHERE vend_id = 'DLL01';
                """)
            """
            返回某列过滤后的平均值
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'avg_price': Decimal('3.865000')}
                """

    # 9.1.2 COUNT()函数
    def test_count_func(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS num_cust 
                FROM Customers;
                """)
            """
            - 使用COUNT(*)对表中行的数目进行计数,不管表列中包含的是空值(NULL)还是非空值.
            - 使用COUNT(column)对特定列中具有值的行进行计数, 忽略NULL值.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'num_cust': 5}
                """

            print("=" * 60)

            cursor.execute("""
                SELECT COUNT(cust_email) AS num_cust 
                FROM Customers;
                """)
            """
            - 使用COUNT(column)对特定列中具有值的行进行计数, 忽略NULL值.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)

    # 9.1.3 MAX()函数
    def test_max_func(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MAX(prod_price) AS max_price 
                FROM Products;
                """)
            """
            提示: 对非数值数据使用MAX()
                虽然MAX()一般用来找出最大的数值或日期值,但许多(并非所有)DBMS允许将它用来
                返回任意列中的最大值,包括返回文本列中的最大值.用于文本数据时,MAX()返回按
                该列排序后的最后一行.
            说明: NULL值
                MAX()函数忽略列值为NULL的行.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'max_price': Decimal('11.99')}
                """

    # 9.1.4 MIN()函数
    def test_min_func(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MIN(prod_price) AS min_price 
                FROM Products;
                """)
            """
            提示: 对非数值数据使用MIN()
                虽然MIN()一般用来找出最小的数值或日期值,但许多(并非所有)DBMS允许将它用来
                返回任意列中的最小值,包括返回文本列中的最小值.用于文本数据时,MIN()返回按
                该列排序后的最前一行.
            说明: NULL值
                MIN()函数忽略列值为NULL的行.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'min_price': Decimal('3.49')}
                """

    # 9.1.5 SUM()函数
    def test_sum_func(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(quantity) AS items_ordered
                FROM OrderItems;
                """)
            """
            说明: NULL值
                SUM()函数忽略列值为NULL的行.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'items_ordered': Decimal('1430')}
                """

            print("=" * 60)

            cursor.execute("""
                SELECT SUM(quantity * item_price) AS total_price
                FROM OrderItems;
                """)
            """
            说明: NULL值
                SUM()函数忽略列值为NULL的行.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'total_price': Decimal('5730.70')}
                """

    # 9.2 聚集(聚合)不同值
    def test_different(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT AVG(DISTINCT prod_price) AS avg_price
                FROM Products;
                """)
            """
            - 只包含不同的值, 指定DISTINCT参数.
            注意: DISTINCT不能用于COUNT(*)
                如果指定列名,则DISTINCT能用于COUNT().DISTINCT不能用
                于COUNT(*).类似地,DISTINCT必须使用列名,不能用于计算或表
                达式.
            提示: 将DISTINCT用于MAX()和MIN()
                虽然DISTINCT从技术上可以用于MAX()和MIN(), 但这样做实际上没
                有价值.一个列中的最小值和最大值不管是否只考虑不同值,结果都是相
                同的.
            说明:其他聚合参数
                除了这里介绍的DISTINCT和ALL参数,有的DBMS还支持其他参数,
                如支持对查询结果的子集进行计算的TOP和TOP PERCENT.为了解
                具体的DBMS支持哪些参数, 看相应文档.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'avg_price': Decimal('7.490000')}
                """

    # 9.3 组合聚集(聚合)函数
    def test_combination(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                COUNT(*) AS num_items,
                MAX(prod_price) AS max_price,
                MIN(prod_price) AS min_price,
                AVG(prod_price) AS avg_price
                FROM Products;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {
                    'num_items': 9, 
                    'max_price': Decimal('11.99'),
                    'min_price': Decimal('3.49'), 
                    'avg_price': Decimal('6.823333')
                }
                """
    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to determine the total number of items sold
           (using the quantity column in OrderItems).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(quantity) AS total_quantity
                FROM OrderItems;
                """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(total_quantity=Decimal('1430'))
                """


    def test_exercise2(self):
        """
        2. Modify the statement you just created to determine the total number
           of products with an id (prod_id) BR01 sold.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(quantity) AS prod_item
                FROM OrderItems
                WHERE prod_id = 'BR01';
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_item=Decimal('120'))
                """


    def test_exercise3(self):
        """
        3. Write a SQL statement to determine the price (prod_price) of the most
           expensive item in the Products table which costs no more than 10,
           name the calculated field max_price.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT MAX(prod_price) AS max_price
                FROM Products 
                WHERE prod_price <= 10;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(max_price=Decimal('9.49'))
                """