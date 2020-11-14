#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection, transaction

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

    #
    """
    顾名思义，INSERT用来将行插入（或添加）到数据库表。插入有几种 
    方式：
        - 插人完整的行；
        - 插入行的一部分；
        - 插人某些查询的结果。
    下面逐一介绍这些内容。
    """
    # 15.1.1 插入完整的行
    def test_insert_complete_raw(self):
        with connection.cursor() as cursor:
            """
            INSERT INTO Customers
                VALUES (
                    1000000006, 'Toy Land', '123 Any Street', 'New York', 'NY', '11111', 'USA', NULL, NULL
                );
            """
            """
            提示: INTO关键字
                在某些SQL实现中,跟在INSERT之后的INTO关键字是可选的.但是即使
                不一定需要,最好还是提供这个关键字,这样做将保证SQL代码在DBMS之
                间可移植.
            分析 ▼
                这个例子将一个新顾客插入到Customers表中。存储到表中每一列的数 
                据在VALUES子句中给出，必须给每一列提供一个值。如果某列没有值， 
                如上面的cust_contact和cust_email列，则应该使用NULL值(假定
                表允许对该列指定空值)。各列必须以它们在表定义中出现的次序填充。
            
                虽然这种语法很简单，但并不安全，应该尽量避免使用. 上面的SQL语 
                句高度依赖于表中列的定义次序，还依赖于其容易获得的次序信息。即 
                使可以得到这种次序信息，也不能保证各列在下一次表结构变动后保持
                完全相同的次序.因此，编写依赖于特定列次序的SQL语句是很不安全 
                的，这样做迟早会出问题。
            编写INSERT语句的更安全（不过更烦琐）的方法如下:
            """
            cursor.execute("""
                INSERT INTO Customers(
                    cust_id, 
                    cust_name, 
                    cust_address, 
                    cust_city, 
                    cust_state, 
                    cust_zip, 
                    cust_country, 
                    cust_contact, 
                    cust_email
                )
                VALUES (
                    1000000006,
                    'Toy Land',
                    '123 Any Street',
                    'New York',
                    'NY',
                    '11111',
                    'USA',
                    NULL,
                    NULL
                );
            """)
            """
            这个例子与前一个INSERT语句的工作完全相同，但在表名后的括号里 
            明确给出了列名。在插入行时，DBMS将用VALUES列表中的相应值填 
            入列表中的对应项。VALUES中的第一个值对应于第一个指定列名，第二
            个值对应于第二个列名，如此等等。
            因为提供了列名，VALUES必须以其指定的次序匹配指定的列名，不一定 
            按各列出现在表中的实际次序.其优点是，即使表的结构改变，这条 
            INSERT语句仍然能正确工作。
            
            说明：不能插入同一条记录两次
                如果你尝试了这个例子的两种方法，会发现第二次生成了一条出错消息，
                说ID为1000000006的顾客已经存在。在第一课我们说过，主键的值必
                须有唯一性，而cust_id是主键，DBMS不允许插入相同cust_id值的
                新行。下一个例子也是同样的道理。要想再尝试另一种插入方法，需要
                首先删除掉已经插入的记录。要么就别尝试新方法了，反正记录已经插
                入好。
                
            提示:总是使用列的列表
                不要使用没有明确给出列的INSERT语句.给出列能使SQL代码继续发挥
                作用，即使表结构发生了变化。
            
            注意:小心使用VALUES
                不管使用哪种INSERT语法，VALUES的数目都必须正确。如果不提供列 
                名，则必须给每个表列提供一个值；如果提供列名，则必须给列出的每 
                个列一个值。否则，就会产生一条错误消息，相应的行不能成功插入。
            """
            print(cursor.fetchone())
            cursor.execute("""
            SELECT *
            FROM Customers
            WHERE cust_id = 1000000006;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000006', 'cust_name': 'Toy Land', 'cust_address': '123 Any Street', 'cust_city': 'New York', 'cust_state': 'NY', 'cust_zip': '11111', 'cust_country': 'USA', 'cust_contact': None, 'cust_email': None}
                """

    # 15.1.2 插入部分的行
    def test_insert_part_raw(self):
        """
        假如要给与Jim Jones同一公司的所有顾客发送一封信件。这个查询要求
        首先找出JimJones工作的公司，然后找出在该公司工作的顾客。下面是
        解决此问题的一种方法：
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Customers(
                    cust_id, 
                    cust_name, 
                    cust_address, 
                    cust_city, 
                    cust_state, 
                    cust_zip, 
                    cust_country
                )
                VALUES (
                    1000000006,
                    'Toy Land',
                    '123 Any Street',
                    'New York',
                    'NY',
                    '11111',
                    'USA'
                );
            """)
            """
            注意：省略列
                如果表的定义允许，则可以在INSERT操作中省略某些列。省略的列 
                必须满足以下某个条件.
                - 该列定义为允许NULL值（无值或空值）。
                - 在表定义中给出默认值。这表示如果不给出值，将使用默认值。
            注意：省略所需的值
                如果表中不允许有NULL值或者默认值，这时却省略了表中的值,
                DBMS就会产生生错误消息，相应的行不能成功插入。
            """
            cursor.execute("""
            SELECT *
            FROM Customers
            WHERE cust_id = 1000000006;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000006', 'cust_name': 'Toy Land', 'cust_address': '123 Any Street', 'cust_city': 'New York', 'cust_state': 'NY', 'cust_zip': '11111', 'cust_country': 'USA', 'cust_contact': None, 'cust_email': None}
                """

    # MySQL基础教程4.7.4 插入多行数据
    def test_insert_multi_raw(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Customers(
                    cust_id, 
                    cust_name, 
                    cust_address, 
                    cust_city, 
                    cust_state, 
                    cust_zip, 
                    cust_country
                )
                VALUES (
                    1000000006,
                    'Toy Land',
                    '123 Any Street',
                    'New York',
                    'NY',
                    '11111',
                    'USA'
                ),
                (
                    1000000007,
                    'Toy Land',
                    '123 Any Street',
                    'New York',
                    'NY',
                    '11111',
                    'USA'
                );
            """)

            cursor.execute("""
            SELECT cust_id, cust_name
            FROM Customers
            WHERE cust_id IN (1000000006, 1000000007) ;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000006', 'cust_name': 'Toy Land'}
                {'cust_id': '1000000007', 'cust_name': 'Toy Land'}
                """

    # 15.1.3 插入检索出的数据
    def test_insert_select_data(self):
        """
        加入想把另一表中的顾客列合并到Customers表中,不需要每次读取一行再
        将它用INSERT插入
        """
        pass

    # 15.2 从一个表复制到另一个表(复制表)
    def test_z_create_select(self):
        """
        有一种数据插入不使用INSERT语句。要将一个表的内容复制到一个全
        新的表(运行中创建的表)，可以使用CREATE SELECT语句(或者在
        SQLServer里也可用SELECT INTO语句) 。

        说明：DB2不支持
            DB2不支持这里描述的CREATE SELECT。

        与INSERT SELECT将数据添加到一个已经存在的表不同，CREATE
        SELECT将数据复制到一个新表(有的DBMS可以覆盖已经存在的表，
        这依赖于所使用的具体DBMS) 。

        下面的例子说明如何使用CREATE SELECT：
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE OrdersCopy AS SELECT * FROM Orders;
            """)
            # 这种复制方法不能复制AUTO_INCREMENT等属性. AUTO_INCREMENT等属性需要在复制后再次进行设置.
            # 复制后VARCHAR(100)甚至可能会变成CHAR(100)
            # 因此必须复制后用DESC确认表的结构.
            cursor.execute("""
                SELECT * FROM OrdersCopy;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)

            print("=" * 60)
            # 排序后复制
            cursor.execute("""
                CREATE TABLE OrdersCopy2 AS 
                SELECT * 
                FROM Orders 
                ORDER BY order_num DESC 
                LIMIT 2 
                OFFSET 1;
            """)
            cursor.execute("""
                SELECT * FROM OrdersCopy2;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20008, order_date=datetime.datetime(2020, 2, 3, 0, 0), cust_id='1000000005')
                Result(order_num=20007, order_date=datetime.datetime(2020, 1, 30, 0, 0), cust_id='1000000004')
                """

    # 7.3 仅复制表的列结构(MySQL基础教程)
    def test_z_create_like(self):
        # 只复制列结构, 不复制数据记录.
        with connection.cursor() as cursor:
            # 该方法会复制AUTO_INCREMENT和PRIMARY KEY等列的属性.
            cursor.execute("""
                CREATE TABLE OrdersCopy LIKE Orders;
            """)

    # 7.4.1 复制其他表的记录(MySQL基础教程)
    def test_z_insert_into_select(self):
        # 初始化新表
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE OrdersCopy LIKE Orders;
            """)

            # 只复制数据记录, 不复制列结构.
            cursor.execute("""
                  INSERT INTO OrdersCopy SELECT * FROM Orders;
              """)

            cursor.execute("""
                SELECT * FROM OrdersCopy;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)

    # 课后练习
    def test_exercise1(self):
        """
        1. Using INSERT and columns specified, add yourself to the Customers table.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Customers(
                    cust_id, 
                    cust_name, 
                    cust_address, 
                    cust_city, 
                    cust_state, 
                    cust_zip, 
                    cust_country
                )
                VALUES (
                    1000000007,
                    'Me Gustas',
                    '广东',
                    '广州',
                    'GD',
                    '529999',
                    'CHA'
                );
            """)
            cursor.execute("""
            SELECT *
            FROM Customers
            WHERE cust_id = 1000000007;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_id': '1000000007', 'cust_name': 'Me Gustas', 'cust_address': '广东', 'cust_city': '广州', 'cust_state': 'GD', 'cust_zip': '529999', 'cust_country': 'CHA', 'cust_contact': None, 'cust_email': None}
                """

    def test_z_exercise2(self):
        """
        2. Make a backup copy of your Orders and OrderItems tables.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE OrdersCopy AS SELECT * FROM Orders;
            """)
            cursor.execute("""
                CREATE TABLE OrderItemsCopy AS SELECT * FROM OrderItems;
            """)
            cursor.execute("""
                SELECT *
                FROM OrdersCopy;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, order_date=datetime.datetime(2020, 5, 1, 0, 0), cust_id='1000000001')
                Result(order_num=20006, order_date=datetime.datetime(2020, 1, 12, 0, 0), cust_id='1000000003')
                Result(order_num=20007, order_date=datetime.datetime(2020, 1, 30, 0, 0), cust_id='1000000004')
                Result(order_num=20008, order_date=datetime.datetime(2020, 2, 3, 0, 0), cust_id='1000000005')
                Result(order_num=20009, order_date=datetime.datetime(2020, 2, 8, 0, 0), cust_id='1000000001')
                """
