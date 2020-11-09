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

    # 8.1 函数
    """
    DBMS函数的差异:
    提取字符串的组成部分(函数):
        DB2:        SUBSTR()          MariaDB:      SUBSTRING()
        Oracle:     SUBSTR()          MySQL:        SUBSTRING()
        PostgreSQL: SUBSTR()          SQL Server:   SUBSTRING()
        SQLite:     SUBSTR()
        
    数据类型转换(函数):
        DB2:        CAST()            MariaDB:      CONVERT()
        Oracle:     CAST()            MySQL:        CONVERT()
        PostgreSQL: CAST()            SQL Server:   CONVERT()
        SQLite:     CAST()     
        
    取当前日期(函数):
        DB2:        CURRENT_DATE()    MariaDB:      CURDATE()
        Oracle:     SYSDATE()         MySQL:        CURDATE()
        PostgreSQL: CURRENT_DATE()    SQL Server:   GETDATE()
        SQLite:     DATE()     
        
    为了代码的可移植,许多SQL程序员不赞成使用特定于实现的功能.虽然这样做很有好处,
    但有的时候并不利于应用程序的性能.如果不使用这些函数,编写某些应用程序代码会很
    艰难.必须利用其他方法来实现DBMS可以非常有效完成的工作.           
    """

    # 8.2 使用函数
    """
    大多数SQL实现支持以下类型的函数.
    - 用于处理文本字符串(如删除或填充值,转换值为大写或小写)的文本函数.
    - 用于在数值数据上进行算术操作(如返回绝对值,进行代数运算)的数值函数.
    - 用于处理日期和时间值并从这些值中提取特定成分(如返回两个日期之差,检
      查日期有效性)的日期和时间函数.
    - 用于生成美观好懂的输出内容的格式化函数(如用语言形式表达出日期,用货
      币符号和千分位表示金额).
    """

    # 8.2.1 文本处理函数
    def test_text_processing_func(self):
        """
        最常使用得通配符是百分号(%).在搜索串中,%表示任何字符串出现任意次数.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_name, UPPER(vend_name) AS vend_name_upcase
                FROM Vendors 
                ORDER BY vend_name;
            """)
            """
            UPPER()将文本转换为大写, 大写后的新列需要赋予新列名(譬如):vend_name_upcase
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_name='Bear Emporium', vend_name_upcase='BEAR EMPORIUM')
                Result(vend_name='Bears R Us', vend_name_upcase='BEARS R US')
                Result(vend_name='Doll House Inc.', vend_name_upcase='DOLL HOUSE INC.')
                Result(vend_name='Fun and Games', vend_name_upcase='FUN AND GAMES')
                Result(vend_name='Furball Inc.', vend_name_upcase='FURBALL INC.')
                Result(vend_name='Jouets et ours', vend_name_upcase='JOUETS ET OURS')
                """
            """
            常用的文本处理函数
            LEFT()                         返回字符串左边的字符
            RIGHT()                        返回字符串右边的字符
            LENGTH()或LEN()或DATALENGTH()   返回字符串的长度
            UPPER()                        将字符串转换为大写
            LOWER()                        将字符串转换为小写
            LTRIM()                        去掉字符串左边的空格
            RTRIM()                        去掉字符串右边的空格
            TRIM()                         去掉字符串两边的空格
            SUBSTR()或SUBSTRING()           提取字符串的组成部分
            SOUNDEX()                      返回字符串的SOUNDEX值
            """

    # 8.2.1(2) SOUNDEX函数
    def test_soundex_func(self):
        """
        SOUNDEX是一个将任何文本字符串转化为描述其语音表示的字母数字模式的算法.
        SOUNDEX考虑了类似的发音字符和音节,使得能对字符串进行发音比较而不是字母
        比较.虽然SOUNDEX不是SQL概念,但多数DBMS都提供对SOUNDEX的支持.

        说明: SOUNDEX支持
            PostgreSQL不支持SOUNDEX(),另外,如果在创建SQLite时使用了
            SQLITE_SOUNDEX编译时选项,那么SOUNDEX()在SQLite中就可用.
            因为SQLITE_SOUNDEX不是默认的编译时选项, 所以多数SQLite实
            现不支持SOUNDEX().
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, cust_contact
                FROM Customers 
                WHERE SOUNDEX(cust_contact) = SOUNDEX('Michell Green');
            """)
            """
            WHERE子句使用SOUNDEX()函数把cust_contact列值和搜索字符串转换为它们的
            SOUNDEX值.因为Michael Green和Michelle Green发音相似,所以它们的
            SOUNDEX值匹配,因此WHERE子句正确地过滤出了所需的数据.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_name='Kids Place', cust_contact='Michelle Green')
                """

    # 8.2.2 日期和时间处理函数
    def test_date_and_time_func(self):
        with connection.cursor() as cursor:
            """MySQL, DB2, MariaDB版本"""
            cursor.execute("""
                SELECT order_num, order_date
                FROM Orders
                WHERE YEAR(order_date) = 2020;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, order_date=datetime.datetime(2020, 5, 1, 0, 0))
                Result(order_num=20006, order_date=datetime.datetime(2020, 1, 12, 0, 0))
                Result(order_num=20007, order_date=datetime.datetime(2020, 1, 30, 0, 0))
                Result(order_num=20008, order_date=datetime.datetime(2020, 2, 3, 0, 0))
                Result(order_num=20009, order_date=datetime.datetime(2020, 2, 8, 0, 0))                
                """

            """SQL Server版本"""
            """
                SELECT order_num, order_date
                FROM Orders
                WHERE DATEPART(yy, order_date) = 2020;
            """

            """PostgreSQL版本"""
            """
                SELECT order_num, order_date
                FROM Orders
                WHERE DATE_PART('year', order_date) = 2020;
            """

            """Oracle, MySQL, PostgreSQL版本"""
            """
                SELECT order_num, order_date
                FROM Orders
                WHERE EXTRACT(year FROM order_date) = 2020;
            """

            """Oracle版本"""
            """
                SELECT order_num, order_date
                FROM Orders
                WHERE order_date BETWEEN to_date('2020-01-01', 'yyyy-mm-dd')
                AND to_date('2020-12-31', 'yyyy-mm-dd');
            """

    # 8.2.3 数值处理函数
    """
    数值处理函数仅处理数值数据.这些函数一般主要用于代数,三角或几何运算,因此不像字符串
    或日期-时间处理函数使用那么频繁.
    
    ABS()   返回一个数的绝对值
    COS()   返回一个角度的余弦
    EXP()   返回一个数的指数值
    PI()    返回圆周率π的值
    SIN()   返回一个角度的正弦
    SQRT()  返回一个数的平方根
    TAN()   返回一个角度的正切
    """

    # 课后练习
    def test_exercise1(self):
        """
        1. Our store is now online and customer accounts are being created.
           Each user needs a login, and the default login will be a
           combination of their name and city. Write a SQL statement that
           returns customer id (cust_id), customer name (cust_name) and
           user_login which is all upper case and comprised of the first
           two characters of the customer contact (cust_contact) and the
           first three characters of the customer city (cust_city). So,
           for example, my login (Ben Forta living in Oak Park) would be
           BEOAK. Hint, for this one you’ll use functions, concatenation,
           and an alias.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                cust_id, 
                cust_name AS customer_name,
                UPPER(CONCAT(LEFT(cust_contact, 2), LEFT(cust_city, 3))) AS user_login 
                FROM Customers;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000001', customer_name='Village Toys', user_login='JODET')
                Result(cust_id='1000000002', customer_name='Kids Place', user_login='MICOL')
                Result(cust_id='1000000003', customer_name='Fun4All', user_login='JIMUN')
                Result(cust_id='1000000004', customer_name='Fun4All', user_login='DEPHO')
                Result(cust_id='1000000005', customer_name='The Toy Store', user_login='KICHI')
                """


    def test_exercise2(self):
        """
        2. Write a SQL statement to return the order number (order_num) and
           order date (order_date) for all orders placed in January 2020,
           sorted by order date. You should be able to figure this out based
           on what you have learned thus far, but feel free to consult your
           DBMS documentation as needed.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, order_date
                FROM Orders
                WHERE (YEAR(order_date) = 2020 AND MONTH(order_date) = 1)
                ORDER BY order_date
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20006, order_date=datetime.datetime(2020, 1, 12, 0, 0))
                Result(order_num=20007, order_date=datetime.datetime(2020, 1, 30, 0, 0))
                """
