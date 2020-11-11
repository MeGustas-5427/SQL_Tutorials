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

    # 14.2.1 使用UNION
    def test_union(self):
        """
        使用UNION很简单，所要做的只是给出每条SELECT语句，在各条语句
        之间放上关键字UNION。
        """
        with connection.cursor() as cursor:
            """
            举个例子，假如需要Illinois、Indiana和Michigan等美国几个州的所有顾
            客的报表，还想包括不管位于哪个州的所有的FuMAll。当然可以利用 
            WHERE子句来完成此工作，不过这次我们使用UNI0N。
            """
            # cursor.execute("""
            #     SELECT cust_name, cust_contact, cust_email
            #     FROM Customers
            #     WHERE cust_state IN ('IL', 'IN', 'MI') OR cust_name = 'Fun4All';
            # """)
            """
            分析 ▼
                第一条SELECT把Illinois、Indiana、Michigan等州的缩写传递给IN子句，
                检索出这些州的所有行。第二条SELECT利用简单的相等测试找出所有 
                Fun4All.你会发现有一条记录出现在两次结果里，因为它满足两次的
                条件。
                组合这两条语句，可以如下进行:
            """
            cursor.execute("""
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_state IN ('IL', 'IN', 'MI')
                UNION
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_name = 'Fun4All';
            """)
            """
            在这个简单的例子中，使用UNION可能比使用WHERE子句更为复杂.但 
            对于较复杂的过滤条件，或者从多个表（而不是一个表）中检索数据的 
            情形，使用UNION可能会使处理更简单。
            提示: UNION的限制
                使用UNION组合SELECT语句的数目，SQL没有标准限制。但是，最 
                好是参考一下具体的DBMS文档，了解它是否对UNION能组合的最大 
                语句数目有限制。
            注意: 性能问题
                多数好的DBMS使用内部查询优化程序，在处理各条SELECT语句前 
                组合它们，理论上讲，这意味着从性能上看使用多条WHERE子句条件 
                还是UNION应该没有实际的差别。不过我说的是理论上，实践中多数 
                查询优化程序并不能达到理想状态，所以最好测试一下这两种方法，
                看哪种工作得更好。
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys', cust_contact='John Smith', cust_email='sales@villagetoys.com')
                Result(cust_name='Fun4All', cust_contact='Jim Jones', cust_email='jjones@fun4all.com')
                Result(cust_name='The Toy Store', cust_contact='Kim Howard', cust_email=None)
                Result(cust_name='Fun4All', cust_contact='Denise L. Stephens', cust_email='dstephens@fun4all.com')
                """

    # 14.2.2 UNION 规则
    """
    可以看到，UNION非常容易使用，但在进行组合时需要注意几条规则。
    - UNION必须由两条或两条以上的SELECT语句组成，语句之间用关键字 
      UNION分隔(因此，如果组合四条SELECT语句，将要使用三个UNION 
      关键字)。
    - UNION中的每个查询必须包含相同的列、表达式或聚集函数（不过， 
      各个列不需要以相同的次序列出）。
    - 列数据类型必须兼容：类型不必完全相同，但必须是DBMS可以隐含 
      转换的类型(例如，不同的数值类型或不同的日期类型).
    
    说明：UNION的列名
        如果结合UNION使用的SELECT语句遇到不同的列名，那么会返回什么名
        字呢？比如说，如果一条语句是SELECT prod_name，而另一条语句是
        SELECT productname，那么查询结果返回的是什么名字呢？
        
        答案是它会返回第一个名字，举的这个例子就会返回prod_name,而不管
        第二个不同的名字。这也意味着你可以对第一个名字使用别名，因而返回
        一个你想要的名字。
        
        这种行为带来一个有意思的副作用。由于只使用第一个名字，那么想要排
        序也只能用这个名字。拿我们的例子来说，可以用
        ORDER BY prod_name对结果排序，如果写成ORDER BY productname
        就会出错，因为查询结果里没有叫作productname的列。
        
        如果遵守了这些基本规则或限制，则可以将UNION用于任何数据检索操作。
    """

    # 14.2.3 包含或取消重复的行
    def test_duplicate_rows(self):
        with connection.cursor() as cursor:
            """如果想返回所有的匹配行，可使用UNION ALL而不是UNION。"""
            cursor.execute("""
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_state IN ('IL', 'IN', 'MI')
                UNION ALL
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_name = 'Fun4All';
            """)
            """
            分析 ▼
                使用UNION ALL，DBMS不取消重复的行. 因此，这里返回5行，其中
                有一行出现两次。
            提示：UNION 与 WHERE
                UNION几乎总是完戒与多个WHERE条件相同的工作。UNION ALL为
                UNION的一种形式，它完成WHERE子句完成不了的工作。如果确实需
                要每个条件的匹配行全部出现（包括重复行），就必须使用
                UNION ALL而不是WHERE。
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys', cust_contact='John Smith', cust_email='sales@villagetoys.com')
                Result(cust_name='The Toy Store', cust_contact='Kim Howard', cust_email=None)
                Result(cust_name='Fun4All', cust_contact='Jim Jones', cust_email='jjones@fun4all.com')
                Result(cust_name='Fun4All', cust_contact='Jim Jones', cust_email='jjones@fun4all.com')
                Result(cust_name='Fun4All', cust_contact='Denise L. Stephens', cust_email='dstephens@fun4all.com')
                """

    # 14.2.4 对组合查询结果排序
    def test_order_by_union(self):
        """
        SELECT语句的输出用ORDER BY子句排序。在用UNION组合查询时，只
        能使用一条ORDER BY子句，它必须位于最后一条SELECT语句之后。对
        于结果集，不存在用一种方式排序一部分，而又用另一种方式排序另一
        部分的情况，因此不允许使用多条ORDER BY子句。
        下面的例子对前面UNION返回的结果进行排序:
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_state IN ('IL', 'IN', 'MI')
                UNION ALL
                SELECT cust_name, cust_contact, cust_email
                FROM Customers
                WHERE cust_name = 'Fun4All'
                ORDER BY cust_name, cust_contact;
            """)
            """
            这条UNION在最后一条SELECT语句后使用了 ORDER BY子句。虽然ORDER BY
            子句似乎只是最后一条SELECT语句的组成部分，但实际上DBMS将用它来排序所
            有SELECT语句返回的所有结果。
            说明：其他类型的UNION
                某些DBMS还支持另外两种UNION: EXCEPT (有时称为MINUS)可用 
                来检索只在第一个表中存在而在第二个表中不存在的行;而INTERSECT 
                可用来检索两个表中都存在的行。实际上，这些UNION很少使用，因 
                为相同的结果可利用联结得到。
            提示：操作多个表
                为了简单，本课中的例子都是使用UNION来组合针对同一表的多个查 
                询。实际上，UMI0N在需要组合多个表的数据时也很有用，即使是有 
                不匹配列名的表，在这种情况下，可以将UNION与别名组合，检索 
                一个结果集.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Fun4All', cust_contact='Denise L. Stephens', cust_email='dstephens@fun4all.com')
                Result(cust_name='Fun4All', cust_contact='Jim Jones', cust_email='jjones@fun4all.com')
                Result(cust_name='Fun4All', cust_contact='Jim Jones', cust_email='jjones@fun4all.com')
                Result(cust_name='The Toy Store', cust_contact='Kim Howard', cust_email=None)
                Result(cust_name='Village Toys', cust_contact='John Smith', cust_email='sales@villagetoys.com')
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement that combines two SELECT statements that retrieve product
           id (prod_id) and quantity from the OrderItems table, one filtering for rows with
           a quantity of exactly 100, and the other filtering for products with an ID that
           begins with BNBG. Sort the results by product id.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, quantity
                FROM OrderItems
                WHERE quantity = 100
                UNION 
                SELECT prod_id, quantity
                FROM OrderItems
                WHERE prod_id LIKE 'BNBG%'
                ORDER BY prod_id;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BNBG01', quantity=100)
                Result(prod_id='BNBG01', quantity=10)
                Result(prod_id='BNBG01', quantity=250)
                Result(prod_id='BNBG02', quantity=100)
                Result(prod_id='BNBG02', quantity=10)
                Result(prod_id='BNBG02', quantity=250)
                Result(prod_id='BNBG03', quantity=100)
                Result(prod_id='BNBG03', quantity=10)
                Result(prod_id='BNBG03', quantity=250)
                Result(prod_id='BR01', quantity=100)
                Result(prod_id='BR03', quantity=100)
                """

    def test_exercise2(self):
        """
        2. Rewrite the SQL statement you just created to use a single SELECT statement.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, quantity
                FROM OrderItems
                WHERE quantity = 100 OR prod_id LIKE 'BNBG%'
                ORDER BY prod_id;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)

    def test_exercise3(self):
        """
        3. This one is a little nonsensical, I know, but it does reinforce a note
           earlier in this lesson. Write a SQL statement which returns and combines
           product name (prod_name) from Products and customer name (cust_name)
           from Customers, and sort the result by product name.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name
                FROM Products
                UNION 
                SELECT cust_name
                FROM Customers
                ORDER BY prod_name;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='12 inch teddy bear')
                Result(prod_name='18 inch teddy bear')
                Result(prod_name='8 inch teddy bear')
                Result(prod_name='Bird bean bag toy')
                Result(prod_name='Fish bean bag toy')
                Result(prod_name='Fun4All')
                Result(prod_name='Kids Place')
                Result(prod_name='King doll')
                Result(prod_name='Queen doll')
                Result(prod_name='Rabbit bean bag toy')
                Result(prod_name='Raggedy Ann')
                Result(prod_name='The Toy Store')
                Result(prod_name='Village Toys')
                """

    def test_exercise4(self):
        """
        4. What is wrong with the following SQL statement? (Try to figure it out
           without running it):
        """
        """
        SELECT cust_name, cust_contact, cust_email
        FROM Customers
        WHERE cust_state  = 'MI'
        ORDER BY cust_name;
        UNION
        SELECT cust_name, cust_contact, cust_email
        FROM Customers
        WHERE cust_state = 'IL'
        ORDER BY cust_name;
        """
