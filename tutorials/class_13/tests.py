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

    # 13.1 使用表别名
    def test_table_alias(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, cust_contact
                FROM Customers C, Orders O, OrderItems OI
                WHERE C.cust_id = O.cust_id
                AND OI.order_num = O.order_num
                AND prod_id = 'RGAN01'
            """)

            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_name': 'Fun4All', 'cust_contact': 'Denise L. Stephens'}
                {'cust_name': 'The Toy Store', 'cust_contact': 'Kim Howard'}
                """

    # 13.2.1 自联结
    def test_self_join(self):
        """
        假如要给与Jim Jones同一公司的所有顾客发送一封信件。这个查询要求
        首先找出JimJones工作的公司，然后找出在该公司工作的顾客。下面是
        解决此问题的一种方法：
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT C1.cust_name, C1.cust_contact, C2.cust_contact AS contact2
                FROM Customers C1
                INNER JOIN Customers C2 ON C1.cust_name = C2.cust_name
                WHERE C2.cust_contact = 'Jim Jones'
                ORDER BY C1.cust_name;
                """)
            """
            提示：用自联结而不用子查询
                自联结通常作为外部语句，用来替代从相同表中检索数据的使用子查
                询语句. 虽然最终的结果是相同的，但许多DBMS处理联结远比处理
                子查询快得多应该试一下两种方法，以确定哪一种的性能更好。
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000003', 'cust_name': 'Fun4All', 'cust_contact': 'Jim Jones'}
                {'cust_id': '1000000004', 'cust_name': 'Fun4All', 'cust_contact': 'Denise L. Stephens'}
                """

            print("=" * 60)

            cursor.execute("""
                SELECT C1.cust_name, C1.cust_contact, C2.cust_contact AS contact2
                FROM Customers C1
                INNER JOIN Customers C2 ON C1.cust_name = C2.cust_name
                # WHERE C2.cust_contact = 'Jim Jones'
                ORDER BY C1.cust_name;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                # 因为cust_name存在两个相同, cust_contact存在差异, 因此自联结利用这个机制而生(n的平方)
                {'cust_name': 'Fun4All', 'cust_contact': 'Denise L. Stephens', 'contact2': 'Jim Jones'}
                {'cust_name': 'Fun4All', 'cust_contact': 'Jim Jones', 'contact2': 'Jim Jones'}

                {'cust_name': 'Fun4All', 'cust_contact': 'Denise L. Stephens', 'contact2': 'Denise L. Stephens'}
                {'cust_name': 'Fun4All', 'cust_contact': 'Jim Jones', 'contact2': 'Denise L. Stephens'}

                {'cust_name': 'Kids Place', 'cust_contact': 'Michelle Green', 'contact2': 'Michelle Green'}
                {'cust_name': 'The Toy Store', 'cust_contact': 'Kim Howard', 'contact2': 'Kim Howard'}
                {'cust_name': 'Village Toys', 'cust_contact': 'John Smith', 'contact2': 'John Smith'}
                """


    # 13.2.2 自然联结
    def test_natural_join(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price 
                FROM Customers C
                INNER JOIN Orders O on C.cust_id = O.cust_id
                INNER JOIN OrderItems OI on O.order_num = OI.order_num
                WHERE OI.prod_id = 'RGAN01'
                """)
            """
            分析 ▼
                在这个例子中，通配符只对第一个表使用。所有其他列明确列出，所以 
                没有重复的列被检索出来。
                事实上，我们迄今为止建立的每个内联结都是自然联结，很可能永远都 
                不会用到不是自然联结的内联结。
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000004', 'cust_name': 'Fun4All', 'cust_address': '829 Riverside Drive', 'cust_city': 'Phoenix', 'cust_state': 'AZ', 'cust_zip': '88888', 'cust_country': 'USA', 'cust_contact': 'Denise L. Stephens', 'cust_email': 'dstephens@fun4all.com', 'order_num': 20007, 'order_date': datetime.datetime(2020, 1, 30, 0, 0), 'prod_id': 'RGAN01', 'quantity': 50, 'item_price': Decimal('4.49')}
                {'cust_id': '1000000005', 'cust_name': 'The Toy Store', 'cust_address': '4545 53rd Street', 'cust_city': 'Chicago', 'cust_state': 'IL', 'cust_zip': '54545', 'cust_country': 'USA', 'cust_contact': 'Kim Howard', 'cust_email': None, 'order_num': 20008, 'order_date': datetime.datetime(2020, 2, 3, 0, 0), 'prod_id': 'RGAN01', 'quantity': 5, 'item_price': Decimal('4.99')}
                """

    # 13.2.3 外联结
    def test_outer_join(self):
        """
        许多联结将一个表中的行与另一个表中的行相关联，但有时候需要包含
        没有关联行的那些行。例如，可能需要使用联结完成以下工作：
            - 对每个顾客下的订单进行计数，包括那些至今尚未下订单的顾客；
            - 列出所有产品以及订购数量，包括没有人订购的产品；
            - 计算平均销售规模，包括那些至今尚未下订单的顾客。
        在上述例子中，联结包含了那些在相关表中没有关联行的行。这种联结
        称为外联结。
        """
        with connection.cursor() as cursor:
            """
            # 注意：语法差别
            # 需要注意，用来创建外联结的语法在不同的SQL实现中可能稍有不
            # 同。下面段落中描述的各种语法形式覆盖了大多数实现，在继续学习
            # 之前请参阅你使用的DBMS文档，以确定其语法。
            # 下面的SELECT语句给出了一个简单的内联结。它检索所有顾客及其订单:
            """
            # cursor.execute("""
            #     SELECT Customers.cust_id, O.order_num
            #     FROM Customers
            #     INNER JOIN Orders O on Customers.cust_id = O.cust_id;
            #     """)
            cursor.execute("""
                SELECT Customers.cust_id, O.order_num 
                FROM Customers
                LEFT OUTER JOIN Orders O on Customers.cust_id = O.cust_id;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000001', 'order_num': 20005}
                {'cust_id': '1000000001', 'order_num': 20009}
                {'cust_id': '1000000002', 'order_num': None}
                {'cust_id': '1000000003', 'order_num': 20006}
                {'cust_id': '1000000004', 'order_num': 20007}
                {'cust_id': '1000000005', 'order_num': 20008}
                """
            """
            分析 ▼
                类似上一课提到的内联结， 这条SELECT语句使用了关键字OUTER JOIN 
                来指定联结类型(而不是在WHERE子句中指定)。但是，与内联结关联 
                两个表中的行不同的是，外联结还包括没有关联行的行。在使用OUTER 
                JOIN语法时，必须使用RIGHT或LEFT关键字指定包括其所有行的表 
                (RIGHT指出的是OUTER JOIN右边的表，而LEFT指出的是OUTER JOIN 
                左边的表)。上面的例子使用LEFT OUTER JOIN从FROM子句左边的表 
                (Customers表)中选择所有行。为了从右边的表中选择所有行， 需要使  
                用 RIGHT OUTER JOIN
            注意:SQUte外联结
                SQLite 支持 LEFT OUTER JOIN，但不支持 RIGHT OUTER JOIN 幸好，
                如果你确实需要在SQLite中使用RIGHT OUTER ]OIN，有一种更简单
                的办法，这将在下面的提示中介绍。
            提示:外联结的类型
                要记住，总是有两种基本的外联结形式：左外联结和右外联结. 它们之间的唯一
                差别是所关联的表的顺序. 换句话说,调整FROM或WHERE子句中表的顺序，左外
                联结可以转换为右外联结因此，这两种外联结可以互换使用，哪个方便就用哪个.
            """

    # 13.2.4 全外联结
    # MySQL, MariaDB, SQLite不支持FULL OUTER JOIN 语法
    # with connection.cursor() as cursor:
    #     cursor.execute("""
    #         SELECT Customers.cust_id, O.order_num
    #         FROM Customers
    #         FULL OUTER JOIN Orders O on Customers.cust_id = O.cust_id;
    #         """)

    # 13.3 使用带聚集(聚合)函数的联结
    def test_group_by_connection(self):
        """
        聚合函数也可以与联结一起使用.

        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT Customers.cust_id, COUNT(O.order_num) AS num_ord
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id
                GROUP BY Customers.cust_id;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """

                """
            """
            分析 ▼
                这条SELECT语句使用INNER JOIN将Customers和Orders表互相关联。 
                GROUP BY子句按顾客分组数据，因此，函数调用COUNT(O.order_num)
                对每个顾客的订单计数，将它作为num_ord返回。
            """
            print("=" * 60)

            # 聚集函数也可以方便地与其他联结一起使用。请看下面的例子
            cursor.execute("""
                SELECT Customers.cust_id, COUNT(O.order_num) AS num_ord
                FROM Customers
                LEFT OUTER JOIN Orders O on Customers.cust_id = O.cust_id
                GROUP BY Customers.cust_id;
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """

                """
            """
            分析 ▼
                这个例子使用左外部联结来包含所有顾客,甚至包含那些没有任何订单
                的顾客◦结果中也包含了顾客1000000002,他有0个订单，这和使用 
                INNER JOIN 时不同。
            
            使用联结和联结条件
                在总结讨论联结的这两课前，有必要汇总一下联结及其使用的要点。
                - 注意所使用的联结类型。一般我们使用内联结，但使用外联结也有效。 
                - 关于确切的联结语法，应该查看具体的文档，看相应的DBMS支持何 
                  种语法(大多数DBMS使用这两课中描述的某种语法)。
                - 保证使用正确的联结条件（不管采用哪种语法），否则会返回不正确 
                  的数据。
                - 应该总是提供联结条件，否则会得出笛卡儿积。
                - 在一个联结中可以包含多个表，甚至可以对每个联结采用不同的联结 
                  类型。虽然这样做是合法的，一般也很有用，但应该在一起测试它们 
                  前分别测试每个联结。这会使故障排除更为简单。
            """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement using an INNER JOIN to retrieve customer name
           (cust_name in Customers) and all order numbers (order_num in Orders)
           for each.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, order_num
                FROM Customers
                INNER JOIN Orders O on Customers.cust_id = O.cust_id;
                """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys', order_num=20005)
                Result(cust_name='Village Toys', order_num=20009)
                Result(cust_name='Fun4All', order_num=20006)
                Result(cust_name='Fun4All', order_num=20007)
                Result(cust_name='The Toy Store', order_num=20008)
                """

    def test_exercise2(self):
        """
        2. Modify the SQL statement you just created to list all customers, even
           those with no orders.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, order_num
                FROM Customers
                LEFT OUTER JOIN Orders O on Customers.cust_id = O.cust_id;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys', order_num=20005)
                Result(cust_name='Village Toys', order_num=20009)
                Result(cust_name='Kids Place', order_num=None)
                Result(cust_name='Fun4All', order_num=20006)
                Result(cust_name='Fun4All', order_num=20007)
                Result(cust_name='The Toy Store', order_num=20008)
                """

    def test_exercise3(self):
        """
        3. Use an OUTER JOIN to join the Products and OrderItems tables, returning
           a sorted list of product names (prod_name) and the order numbers
           (order_num) associated with each.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, order_num
                FROM Products 
                LEFT OUTER JOIN OrderItems OI on Products.prod_id = OI.prod_id
                ORDER BY prod_name;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='12 inch teddy bear', order_num=20006)
                Result(prod_name='18 inch teddy bear', order_num=20005)
                Result(prod_name='18 inch teddy bear', order_num=20006)
                Result(prod_name='18 inch teddy bear', order_num=20007)
                Result(prod_name='18 inch teddy bear', order_num=20008)
                Result(prod_name='8 inch teddy bear', order_num=20005)
                Result(prod_name='8 inch teddy bear', order_num=20006)
                Result(prod_name='Bird bean bag toy', order_num=20007)
                Result(prod_name='Bird bean bag toy', order_num=20008)
                Result(prod_name='Bird bean bag toy', order_num=20009)
                Result(prod_name='Fish bean bag toy', order_num=20007)
                Result(prod_name='Fish bean bag toy', order_num=20008)
                Result(prod_name='Fish bean bag toy', order_num=20009)
                Result(prod_name='King doll', order_num=None)
                Result(prod_name='Queen doll', order_num=None)
                Result(prod_name='Rabbit bean bag toy', order_num=20007)
                Result(prod_name='Rabbit bean bag toy', order_num=20008)
                Result(prod_name='Rabbit bean bag toy', order_num=20009)
                Result(prod_name='Raggedy Ann', order_num=20007)
                Result(prod_name='Raggedy Ann', order_num=20008)
                """

    def test_exercise4(self):
        """
        4. Modify the SQL statement created in the previous challenge so that it
           returns a total of number of orders for each item (as opposed to the
           order numbers).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, COUNT(order_num) AS orders
                FROM Products 
                LEFT OUTER JOIN OrderItems OI on Products.prod_id = OI.prod_id
                GROUP BY prod_name
                ORDER BY prod_name;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='12 inch teddy bear', orders=1)
                Result(prod_name='18 inch teddy bear', orders=4)
                Result(prod_name='8 inch teddy bear', orders=2)
                Result(prod_name='Bird bean bag toy', orders=3)
                Result(prod_name='Fish bean bag toy', orders=3)
                Result(prod_name='King doll', orders=0)
                Result(prod_name='Queen doll', orders=0)
                Result(prod_name='Rabbit bean bag toy', orders=3)
                Result(prod_name='Raggedy Ann', orders=2)
                """

    def test_exercise5(self):
        """
        5. Write a SQL statement to list vendors (vend_id in Vendors) and the number
           of products they have available, including vendors with no products.
           You’ll want to use an OUTER JOIN and the COUNT() aggregate function to count
           the number of products for each in the Products table. Pay attention, the
           vend_id column appears in multiple tables so any time you refer to it you’ll
           need to fully qualify it.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT V.vend_id, COUNT(P.prod_id) AS count
                FROM  Vendors V
                LEFT OUTER JOIN Products P on V.vend_id = P.vend_id
                GROUP BY V.vend_id;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_id='BRE02', count=0)
                Result(vend_id='BRS01', count=3)
                Result(vend_id='DLL01', count=4)
                Result(vend_id='FNG01', count=2)
                Result(vend_id='FRB01', count=0)
                Result(vend_id='JTS01', count=0)
                """
