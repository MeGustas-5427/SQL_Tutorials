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

    # 12.2 创建联结
    def test_create_grouping(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, prod_name, prod_price
                FROM Products, Vendors
                WHERE Vendors.vend_id = Products.vend_id;
            """)

            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_name='Bears R Us', prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(vend_name='Bears R Us', prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(vend_name='Bears R Us', prod_name='18 inch teddy bear', prod_price=Decimal('11.99'))
                Result(vend_name='Doll House Inc.', prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                Result(vend_name='Fun and Games', prod_name='King doll', prod_price=Decimal('9.49'))
                Result(vend_name='Fun and Games', prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 12.2.1 WHERE子句的重要性
    def test_where_is_important(self):
        """
        使用WHERE子句建立联结关系似乎有点奇怪，但实际上是有个很充分的
        理由的。要记住，在一条SELECT语句中联结几个表时，相应的关系是
        在运行中构造的。在数据库表的定义中没有指示DBMS如何对表进行联
        结的内容。你必须自己做这件事情。在联结两个表时，实际要做的是将
        第一个表中的每一行与第二个表中的每一行配对。WHERE子句作为过滤
        条件，只包含那些匹配给定条件（这里是联结条件）的行。没有WHERE
        子句，第一个表中的每一行将与第二个表中的每一行配对，而不管它们
        逻辑上是否能配在一起。

        笛卡儿积（cartesian product)
            由没有联结条件的表关系返回的结果为笛卡儿积。检索出的行的数目
            将是第一个表中的行数乘以第二个表中的行数。
        """

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, prod_name, prod_price
                FROM Vendors, Products;
            """)

            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
            """
            分析 ▼
                从上面的输出可以看到，相应的笛卡儿积不是我们想要的。这里返回的
                数据用每个供应商匹配了每个产品，包括了供应商不正确的产品（即使
                供应商根本就没有产品）。
                
            注意: 不要忘了WHERE子句  
                要保证所有联结都有WHERE子句，否则DBMS将返回比想要的教据多
                得多的数据。同理，要保证WHERE子句的正确性。不正确的过滤条件
                会导致DBMS返回不正确的数据。
            提示：叉联结
                有时，返回笛卡儿积的联结，也称叉联结(cross join)
            """

    # 12.2.2 内联结
    def test_inner_join(self):
        """
        12.2使用的联结称为等值联结（equi join)，它基于两个表之间的相等测试。
        下面这种联结称为内联结（inner join)。其实，可以对这种联结使删微不同
        的语法，明确指定联结的类型。下面的SELECT语句返回与12.2例子完全相同的
        数据：
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, prod_name, prod_price
                FROM Vendors
                INNER JOIN Products ON Vendors.vend_id = Products.vend_id
                # INNER JOIN Products USING(vend_id)  # 若两个联结列的名称相同,可以使用USING简化写法
            """)
            """
            分析 ▼
                此语句中的SELECT与前面的SELECT语句相同，但FROM子句不同。这 
                里,两个表之间的关系是以INNER JOIN指定的部分FROM子句。在使用 
                这种语法时，联结条件用特定的ON子句而不是WHERE子句给出。传递 
                给ON的实际条件与传递给WHERE的相同。至于选用哪种语法，请参阅具
                体的DBMS文档。
            说明：“正确的”语法
                ANSI SQL规范首选INNER JOIN语法，之前使用的是简单的等值语法。
                其实，SQL语言纯正论者是用鄙视的眼光看待简单语法的。这就是说，
                DBMS的确支持简单格式和标准格式，我建议你要理解这两种格式，具体
                使用就看你用哪个更顺手了
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_name='Bears R Us', prod_name='8 inch teddy bear', prod_price=Decimal('5.99'))
                Result(vend_name='Bears R Us', prod_name='12 inch teddy bear', prod_price=Decimal('8.99'))
                Result(vend_name='Bears R Us', prod_name='18 inch teddy bear', prod_price=Decimal('11.99'))
                Result(vend_name='Doll House Inc.', prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                Result(vend_name='Fun and Games', prod_name='King doll', prod_price=Decimal('9.49'))
                Result(vend_name='Fun and Games', prod_name='Queen doll', prod_price=Decimal('9.49'))
                """

    # 12.2.3 联结多个表
    def test_join_multiple_tables(self):
        """
        分析 ▼
            这个例子显示订单20007中的物品。订单物品存储在OrderItems表中
            每个产品按其产品ID存储，它引用Products表中的产品。这些产品通
            过供应商ID联结到Vendors表中相应的供应商，供应商ID存储在每个
            产品的记录中。这里的FROM子句列出三个表，WHERE子句定义这两个联
            结条件，而第三个联结条件用来过滤出订单20007中的物品。
        注意：性能考虑
            DBMS在运行时关联指定的每个表，以处理联结。这种处理可能非常
            耗费资源，因此应该注意，不要联结不必要的表。联结的表越多，性
            能下降越厉害。
        注意：联结中表的最大数目
            虽然SQL本身不限制每个联结约束中表的数目，但实际上许多DBMS
            都有限制。请参阅具体的DBMS文档以了解其限制。
        """

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, prod_name, prod_price
                FROM Vendors, Products, OrderItems
                WHERE Products.vend_id = Vendors.vend_id
                AND OrderItems.prod_id = Products.prod_id
                AND order_num = 20007;
            """)

            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_name='Bears R Us', prod_name='18 inch teddy bear', prod_price=Decimal('11.99'))
                Result(vend_name='Doll House Inc.', prod_name='Fish bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Bird bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Rabbit bean bag toy', prod_price=Decimal('3.49'))
                Result(vend_name='Doll House Inc.', prod_name='Raggedy Ann', prod_price=Decimal('4.99'))
                """

            print("=" * 60)

            # cursor.execute("""
            #     SELECT cust_name, cust_contact
            #     FROM Customers, Orders, OrderItems
            #     WHERE Customers.cust_id = Orders.cust_id
            #     AND Orders.order_num = OrderItems.order_num
            #     AND OrderItems.prod_id = 'RGAN01';
            # """)
            cursor.execute("""
                SELECT cust_name, cust_contact
                FROM Customers
                INNER JOIN Orders O USING(cust_id)
                INNER JOIN OrderItems OI on O.order_num = OI.order_num
                WHERE OI.prod_id = 'RGAN01';
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Fun4All', cust_contact='Denise L. Stephens')
                Result(cust_name='The Toy Store', cust_contact='Kim Howard')
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to return customer name (cust_name) from the Customers
           table and related order numbers (order_num) from the Orders table, sorting
           the result by customer name and then by order number. Actually, try this one
           twice, once using simple equijoin syntax and once using an INNER JOIN.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, order_num
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                Order By 1, 2;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Fun4All', order_num=20006)
                Result(cust_name='Fun4All', order_num=20007)
                Result(cust_name='The Toy Store', order_num=20008)
                Result(cust_name='Village Toys', order_num=20005)
                Result(cust_name='Village Toys', order_num=20009)
                """

    def test_exercise2(self):
        """
        2. Let’s make the previous challenge more useful. In addition to returning the
           customer name and order number, add a third column named OrderTotal containing
           the total price of each order. There are two ways to do this, you can create
           the OrderTotal column using a subquery on the OrderItems table, or you can
           join the OrderItems table to the existing tables and use an aggregate function.
           Here’s a hint, watch out for where you need to use fully qualified column names.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, O.order_num, SUM(OI.item_price*OI.quantity) AS OrderTotal
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                INNER JOIN OrderItems OI on O.order_num = OI.order_num
                GROUP BY O.order_num
                Order By 3;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='The Toy Store', order_num=20008, OrderTotal=Decimal('189.60'))
                Result(cust_name='Fun4All', order_num=20006, OrderTotal=Decimal('329.60'))
                Result(cust_name='Village Toys', order_num=20005, OrderTotal=Decimal('1648.00'))
                Result(cust_name='Fun4All', order_num=20007, OrderTotal=Decimal('1696.00'))
                Result(cust_name='Village Toys', order_num=20009, OrderTotal=Decimal('1867.50'))
                """
            print("=" * 60)
            cursor.execute("""
                SELECT cust_name, O.order_num, (
                    SELECT SUM(OI.quantity * OI.item_price)
                    FROM OrderItems OI
                    WHERE OI.order_num = O.order_num
                ) AS OrderTotal
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                Order By 3;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='The Toy Store', order_num=20008, OrderTotal=Decimal('189.60'))
                Result(cust_name='Fun4All', order_num=20006, OrderTotal=Decimal('329.60'))
                Result(cust_name='Village Toys', order_num=20005, OrderTotal=Decimal('1648.00'))
                Result(cust_name='Fun4All', order_num=20007, OrderTotal=Decimal('1696.00'))
                Result(cust_name='Village Toys', order_num=20009, OrderTotal=Decimal('1867.50'))
                """

    def test_exercise3(self):
        """
        3. Let’s revisit Challenge 1 from Lesson 11. Write a SQL statement that retrieves
           the dates when product BR01 was ordered, but this time use a join and simple
           equijoin syntax. The output should be identical to the one from Lesson 12.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_id, order_date
                FROM Orders
                INNER JOIN OrderItems OI on Orders.order_num = OI.order_num
                WHERE OI.prod_id = 'BR01'
                ORDER BY order_date
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000003', order_date=datetime.datetime(2020, 1, 12, 0, 0))
                Result(cust_id='1000000001', order_date=datetime.datetime(2020, 5, 1, 0, 0))
                """

    def test_exercise4(self):
        """
        4. That was fun, let’s try it again. Recreate the SQL you wrote for Lesson 11 Challenge 3,
           this time using ANSI INNER JOIN syntax. The code you wrote there employed two nested
           subqueries, and to recreate it you’ll need two INNER JOIN statements, each formatted
           like the INNER JOIN example earlier in this lesson. And don’t forget the WHERE clause
           to filter by prod_id.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_email
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                INNER JOIN OrderItems OI on O.order_num = OI.order_num
                WHERE OI.prod_id = 'BR01'
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_email='sales@villagetoys.com')
                Result(cust_email='jjones@fun4all.com')
                """

    def test_exercise5(self):
        """
        5. One more, and to make things more fun we’ll mix joins, aggregates functions, and
           grouping, too. Ready? Back in Lesson 10 I issued you a Challenge to find all order
           numbers with a value of 1000 or more. Those results are useful, but what would be
           even more useful is the name of the customers who placed orders of at least that
           amount. So, write a SQL statement that uses joins to return customer name (cust_name)
           from the Customers table, and the total price of all orders from the OrderItems table.
           Here’s a hint, to join those tables you’ll also need to include the Orders table (as
           Customers is not related directly to OrderItems, Customers is related to Orders and
           Orders is related to OrderItems). Don’t forget the GROUP BY and HAVING, and sort the
           results by customer name. You can use simple equijoin or ANSI INNER JOIN syntax for
           this one. Or, if you are feeling brave, try writing it both ways.

        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, SUM(OI.item_price*OI.quantity) AS order_money
                FROM Customers C
                INNER JOIN Orders O on C.cust_id = O.cust_id
                INNER JOIN OrderItems OI on O.order_num = OI.order_num
                GROUP BY cust_name
                HAVING order_money >= 1000
                ORDER BY cust_name;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Fun4All', order_money=Decimal('2025.60'))
                Result(cust_name='Village Toys', order_money=Decimal('3515.50'))
                """