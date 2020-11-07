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

    # 5.1 组合WHERE子句
    def test_compose_where(self):
        """
        为了进行更强的过滤控制,SQL允许给出多个WHERE子句.这些子句有两种
        使用方式,即以AND子句或OR子句的方式使用.

        操作符(operator)
            用来联结或改变WHERE子句中的子句的关键字, 也称为逻辑操作符(logical operator)
        """
        pass

    # 5.1.1 AND 操作符
    def test_and_operator(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                prod_id, prod_name, prod_price 
                FROM 
                Products 
                WHERE
                vend_id = 'DLL01' AND prod_price <= 4;
                """)
            """
            AND: 用在WHERE子句中的关键字,用来指示检索满足所有给定条件的行.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_id': 'BNBG01', 'prod_name': 'Fish bean bag toy', 'prod_price': Decimal('3.49')}
                {'prod_id': 'BNBG02', 'prod_name': 'Bird bean bag toy', 'prod_price': Decimal('3.49')}
                {'prod_id': 'BNBG03', 'prod_name': 'Rabbit bean bag toy', 'prod_price': Decimal('3.49')}
                """

    # 5.1.2 OR 操作符
    def test_or_operator(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                prod_id, prod_name, prod_price 
                FROM 
                Products 
                WHERE
                vend_id = 'DLL01' OR vend_id = 'BRS01';
                """)
            """
            OR: 与AND相反,OR操作符告诉DBMS匹配任一条件而不是同时匹配两个条件.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_id': 'BR01', 'prod_name': '8 inch teddy bear', 'prod_price': Decimal('5.99')}
                {'prod_id': 'BR02', 'prod_name': '12 inch teddy bear', 'prod_price': Decimal('8.99')}
                {'prod_id': 'BR03', 'prod_name': '18 inch teddy bear', 'prod_price': Decimal('11.99')}
                {'prod_id': 'BNBG01', 'prod_name': 'Fish bean bag toy', 'prod_price': Decimal('3.49')}
                {'prod_id': 'BNBG02', 'prod_name': 'Bird bean bag toy', 'prod_price': Decimal('3.49')}
                {'prod_id': 'BNBG03', 'prod_name': 'Rabbit bean bag toy', 'prod_price': Decimal('3.49')}
                {'prod_id': 'RGAN01', 'prod_name': 'Raggedy Ann', 'prod_price': Decimal('4.99')}
                """

    # 5.1.3 求值顺序
    def test_value_order_by(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                vend_id, prod_price
                FROM 
                Products 
                WHERE
                vend_id = 'DLL01' OR vend_id = 'BRS01' AND prod_price >= 10;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend_id': 'BRS01', 'prod_price': Decimal('11.99')}
                {'vend_id': 'DLL01', 'prod_price': Decimal('3.49')}
                {'vend_id': 'DLL01', 'prod_price': Decimal('3.49')}
                {'vend_id': 'DLL01', 'prod_price': Decimal('3.49')}
                {'vend_id': 'DLL01', 'prod_price': Decimal('4.99')}
                """
            """
            结果:
                返回的行中有4行价格小于10美元, 显然返回的行未按预期的进行过滤.
            错误示范的结果解释:
                原因在于求值的顺序. SQL(像多数语言一样)在处理OR操作符前,优先处理AND操作符.
                当SQL看到上述WHERE子句时,它理解为:由供应商BRS01制造的价格为10美元以上的所
                有产品,以及由供应商DLL01制造的所有产品,而不管其价格如何.
            """

            print("=" * 60)
            cursor.execute("""
                SELECT 
                vend_id, prod_price
                FROM 
                Products 
                WHERE
                (vend_id = 'DLL01' OR vend_id = 'BRS01') AND prod_price >= 10;
                """)
            """
            解决方法: 使用圆括号对操作符进行明确分组. 因为圆括号具有比AND或OR操作符更高的优先级.
            提示:
                任何时候使用具有AND和OR操作符的WHERE子句,都应该使用圆括号
                明确地分组操作符.不要过分依赖默认求值顺序,即使它确实如你希
                望的那样.使用圆括号没有任何坏处,它能消除歧义.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend_id': 'BRS01', 'prod_price': Decimal('11.99')}
                """

    # 5.2 IN 操作符
    def test_in_operator(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                vend_id, prod_name
                FROM 
                Products 
                WHERE
                vend_id IN ('DLL01', 'BRS01');
                """)
            """
            IN操作符完成了与OR相同的功能, 为何要使用IN操作符?
            1. IN操作付一般比一组OR操作符执行得更快.
            2. 在有很多合法选项时,IN操作符的语法更清楚, 更直观.
            3. 在与其他AND和OR操作符组合使用IN时,求值顺序更容易管理.
            4. IN得最大优点是可以包含其他SELECT语句,能够更动态地建立WHERE子句. 第11课会介绍.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend_id': 'BRS01', 'prod_name': '8 inch teddy bear'}
                {'vend_id': 'BRS01', 'prod_name': '12 inch teddy bear'}
                {'vend_id': 'BRS01', 'prod_name': '18 inch teddy bear'}
                {'vend_id': 'DLL01', 'prod_name': 'Fish bean bag toy'}
                {'vend_id': 'DLL01', 'prod_name': 'Bird bean bag toy'}
                {'vend_id': 'DLL01', 'prod_name': 'Rabbit bean bag toy'}
                {'vend_id': 'DLL01', 'prod_name': 'Raggedy Ann'}
                """

    # 5.3 NOT 操作符
    def test_not_operator(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                vend_id, prod_name
                FROM 
                Products 
                WHERE
                NOT 
                vend_id = 'DLL01'
                ORDER BY 
                prod_name;
                """)
            """
            NOT: 该关键字在WHERE子句中用来否定其后条件
                在复杂的子句中, NOT非常有用. 
                譬如, 在与IN操作符联合使用时,NOT可以非常简单地找出与条件列表不匹配得行
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend_id': 'BRS01', 'prod_name': '12 inch teddy bear'}
                {'vend_id': 'BRS01', 'prod_name': '18 inch teddy bear'}
                {'vend_id': 'BRS01', 'prod_name': '8 inch teddy bear'}
                {'vend_id': 'FNG01', 'prod_name': 'King doll'}
                {'vend_id': 'FNG01', 'prod_name': 'Queen doll'}
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to retrieve the vendor name (vend_name) from the
           Vendors table, returning only vendors in California (this requires
           filtering by both country (USA) and state (CA), after all, there could
           be a California outside of the USA). Here’s a hint, the filter
           requires matching strings.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, vend_country, vend_state 
                FROM Vendors 
                WHERE (vend_country = 'USA' AND vend_state = 'CA');
                """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(vend_name='Doll House Inc.', vend_country='USA', vend_state='CA')
                """

    def test_exercise2(self):
        """
        2. Write a SQL statement to find all orders where at least 100 of items BR01,
           BR02, or BR03 were ordered. You’ll want to return order number (order_num),
           product id (prod_id), and quantity for the OrderItems table, filtering by
           both the product id and quantity. Here’s a hint, depending on how you write
           your filter, you may need to pay special attention to order of evaluation.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, order_num , quantity
                FROM OrderItems 
                WHERE (quantity >= 100 AND prod_id IN ('BR01','BR02','BR03'));
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BR01', order_num=20005, quantity=100)
                Result(prod_id='BR03', order_num=20005, quantity=100)
                """

    def test_exercise3(self):
        """
        3. Now let’s revisit a challenge from the previous lesson. Write a SQL statement
           which returns the product name (prod_name) and price (prod_price) from
           Products for all products priced between 3 and 6. Use an AND, and sort the
           results by price.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, prod_price
                FROM Products 
                WHERE (prod_price >= 3 AND prod_price <= 6)
                ORDER BY prod_price;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                Result(prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                """

    def test_exercise4(self):
        """
        4. What is wrong with the following SQL statement? (Try to figure it out without running it):
        SELECT vend_name
        FROM Vendors
        ORDER BY vend_name
        WHERE vend_country = 'USA' AND vend_state = 'CA';
        """
        pass