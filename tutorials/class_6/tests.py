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

    # 6.1 LIKE 操作符
    def test_like_operator(self):
        """
        通配符搜索只能用于文本字段(字符串),非文本数据类型字段不能使用通配符搜索.
        """
        pass

    # 6.1.1 百分号(%)通配符
    def test_percent_sign_wildcard(self):
        """
        最常使用得通配符是百分号(%).在搜索串中,%表示任何字符串出现任意次数.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, prod_name
                FROM Products 
                WHERE prod_name 
                LIKE 'Fish%';
            """)
            """
            此例子使用了搜索模式'Fish%'.在执行这调子句时,将检索任意以Fish起头得词.
            %告诉DBMS接受Fish之后得任意字符,不管它有多少字符.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BNBG01', prod_name='Fish bean bag toy')
                """

            print("=" * 60)

            """根据DBMS的不同及其配置,搜索可以是区分大小写的"""
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT prod_id, prod_name
                    FROM Products 
                    WHERE prod_name 
                    LIKE '%bean bag%';
                """)
                """
                通配符可在搜索模式中的任意位置使用,并且可以使用多个通配符.
                搜索模式'%bean bag%'表示匹配任何位置商包含文本bean bag
                的值,不论它之前或之后出现什么字符.
                """
                for result in namedtuplefetchall(cursor):  # 读取所有
                    print(result)
                    """
                    Result(prod_id='BNBG01', prod_name='Fish bean bag toy')
                    Result(prod_id='BNBG02', prod_name='Bird bean bag toy')
                    Result(prod_id='BNBG03', prod_name='Rabbit bean bag toy')
                    """

            print("=" * 60)

            """通配符也可以出现在搜索模式的中间,虽然这样做不太有用."""
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT prod_id, prod_name
                    FROM Products 
                    WHERE prod_name 
                    LIKE 'F%y';
                """)
                """
                说明: 请注意后面所跟的空格
                    有些DBMS用空格来填补字段的内容.例如,如果某列有50个字符,而存储的文本为
                    Fish bean bag toy(17个字符),则为填满该列需要的文本后附加33个空格.
                    这样做一般对数据及其使用没有影响,但是可以对上述SQL语句有负面影响.子句
                    WHERE prod_name LIKE 'F%y'只匹配以F开头 以y结尾的prod_name.如果
                    值后面有空格,则不是以y结尾,所以Fish bean bag toy就不会检索出来.简单
                    的解决办法是给搜索模式再增加一个%号:'F%y%'还匹配y之后的字符(或空格).
                    更好的解决办法是用函数去掉空格.第8课说.
                    
                注意: 请注意NULL
                    通配符%看起来像是可以匹配任何东西,但有个例外,这就是NULL.
                    子句WHERE prod_name LIKE '%'不会匹配产品名为NULL的行.
                """
                for result in namedtuplefetchall(cursor):  # 读取所有
                    print(result)
                    """
                    Result(prod_id='BNBG01', prod_name='Fish bean bag toy')
                    """

    # 6.1.2 下划线(_)通配符
    def test_underscore_wildcard(self):
        """
        下划线的用途与%一样,但它只匹配单个字符,而不是多个字符.
        说明: DB2不支持通配符_
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, prod_name
                FROM Products 
                WHERE prod_name 
                LIKE '__ inch teddy bear';
            """)

            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BR02', prod_name='12 inch teddy bear')
                Result(prod_id='BR03', prod_name='18 inch teddy bear')
                """

    # 6.1.3 方括号([])通配符
    def test_square_brackets_wildcard(self):
        """
        方括号([])通配符用来指定一个字符集,它必须匹配指定位置(通配符的位置)的一个字符.
        """
        with connection.cursor() as cursor:
            """找出所有名字以J或M开头的联系人."""
            cursor.execute("""
                SELECT cust_contact
                FROM Customers 
                WHERE cust_contact
                LIKE '[JM]%';
            """)

            """可以使用前缀字符^(脱字号)来否定, 譬如查询匹配以J和M之外的任意字符起头的任意联系人名"""
            cursor.execute("""
                SELECT cust_contact
                FROM Customers 
                WHERE cust_contact
                LIKE '^[JM]%';
            """)
            """
            说明: 并不总是支持集合
                与前面描述的通配符不一样,并不是所有DBMS都支持用来创建集合的[].微软
                SQL Server支持集合,但是MySQL,Oracle,DB2,SQLite都不支持.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)

    # 6.2 使用通配符的技巧
    """
    SQL的通配符很有用.但这种功能是有代价的,即通配符搜索一般比前面讨论的其他搜索
    要耗费更长的处理时间.这里给出一些使用通配符时要记住的技巧.
    1. 不要过渡使用通配符.如果其他操作符能达到相同的目的,应该使用其他操作符.
    2. 在确实需要使用通配符时,也尽力不要把他们用在搜索模式的开始处.把通配符
       置于开始处,搜索起来是最慢的.
    3. 仔细注意通配符的位置.如果放错地方,可能不会返回想要的数据.
    """

    # 课后练习
    def test_exercise1(self):
        """
        1. Write a SQL statement to retrieve the product name (prod_name) and
           description (prod_desc) from the Products table, returning only
           products where the word toy is in the description.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, prod_desc 
                FROM Products 
                WHERE prod_desc LIKE '%toy%';
            """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy', prod_desc='Fish bean bag toy, complete with bean bag worms with which to feed it')
                Result(prod_name='Bird bean bag toy', prod_desc='Bird bean bag toy, eggs are not included')
                Result(prod_name='Rabbit bean bag toy', prod_desc='Rabbit bean bag toy, comes with bean bag carrots')
                """

    def test_exercise2(self):
        """
        2. Now let’s flip things around. Write a SQL statement to retrieve the product
           name (prod_name) and description (prod_desc) from the Products table,
           returning only products where the word toy doesn’t appear in the description.
           And this time, sort the results by product name.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, prod_desc 
                FROM Products 
                WHERE prod_desc NOT LIKE '%toy%'
                ORDER BY prod_name;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='12 inch teddy bear', prod_desc='12 inch teddy bear, comes with cap and jacket')
                Result(prod_name='18 inch teddy bear', prod_desc='18 inch teddy bear, comes with cap and jacket')
                Result(prod_name='8 inch teddy bear', prod_desc='8 inch teddy bear, comes with cap and jacket')
                Result(prod_name='King doll', prod_desc='12 inch king doll with royal garments and crown')
                Result(prod_name='Queen doll', prod_desc='12 inch queen doll with royal garments and crown')
                Result(prod_name='Raggedy Ann', prod_desc='18 inch Raggedy Ann doll')
                """

    def test_exercise3(self):
        """
        3. Write a SQL statement to retrieve the product name (prod_name) and description
           (prod_desc) from the Products table, returning only products where both the
           words toy and carrots appear in the description. There are a couple of ways to
           do this, but for this challenge use AND and two LIKE comparisons.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, prod_desc 
                FROM Products 
                WHERE (prod_desc LIKE '%toy%' AND prod_desc LIKE '%carrots%');
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Rabbit bean bag toy', prod_desc='Rabbit bean bag toy, comes with bean bag carrots')
                """

    def test_exercise4(self):
        """
        4. This next one is a little trickier. I didn’t show you this syntax specifically,
           but see if you can figure it out anyway based on what you have learned thus far.
           Write a SQL statement to retrieve the product name (prod_name) and description
           (prod_desc) from the Products table, returning only products where both the
           words toy and carrots appear in the description in that order (the word toy
           before the word carrots). Here’s a hint, you’ll only need one LIKE with 3 %
           symbols to do this.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, prod_desc 
                FROM Products 
                WHERE prod_desc LIKE '%toy%%carrots%';
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Rabbit bean bag toy', prod_desc='Rabbit bean bag toy, comes with bean bag carrots')
                """