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

    # 7.1 计算字段
    def calculated_field(self):
        """存储在数据库表的数据一般不是应用程序所需要的格式"""
        """
        - 需要显示公司名,同时还需要显示公司的地址,但这两个信息存储在不同的表列中.
        - 城市,州和邮政编码存储在不同的列中,但邮件标签打印程序需要把他们作为一个
          有恰当格式的字段检索出来.
        - 列数据是大小写混合的,但报表程序需要把所有数据按大写表示出来.
        - 物品订单表存储物品的价格和数量,不存储每个物品的总价格(用价格×数量即可).
          但为打印发票,需要物品的总价格.
        - 需要根据表数据进行诸如总数,平均数的计算.
        """

    # 7.2 拼接字段
    def test_splicing_field(self):
        with connection.cursor() as cursor:
            """
            把两个列拼接起, 在SQL中的SELECT语句中, 可使用一个特殊的操作符来拼接两个列.
            根据所使用的DBMS, 此操作符可用加号(+)或两个竖杠(||)表示.在MySQL和MariaDB
            中,必须使用特殊的函数
            """
            # 使用MySQL或MariaDB时需要使用的语句:
            cursor.execute("""
                SELECT CONCAT(vend_name, '(', vend_country, ')   ')
                AS vend_title
                FROM Vendors
                ORDER BY vend_name;
            """)
            """
            使用别名:
                新计算列的名字需要一个新名字, SQL支持别名,别名(alias)是一个字段
                或值的替换名.别名用AS关键字赋予.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend_title': 'Bear Emporium(USA)   '}
                {'vend_title': 'Bears R Us(USA)   '}
                {'vend_title': 'Doll House Inc.(USA)   '}
                {'vend_title': 'Fun and Games(England)   '}
                {'vend_title': 'Furball Inc.(USA)   '}
                {'vend_title': 'Jouets et ours(France)   '}
                """
            # 加号用法(多数DBMS的用法):
            """
                SELECT vend_name + '(' + vend_country + ')'
                FROM Vendors
                ORDER BY vend_name;
            """
            # ||号用法:
            """
                SELECT vend_name || '(' || vend_country || ')'
                FROM Vendors
                ORDER BY vend_name;
            """

    # 7.2.1 TRMI函数
    def test_trim_func(self):
        with connection.cursor() as cursor:
            """
            如果想去掉返回的数据不需要的空格.可用使用TRIM函数
            大多数DBMS都支持:
            TRIM() :去掉字符串左右两边的空格.
            LTRIM():去掉字符串左两边的空格.
            RTRIM():去掉字符串右两边的空格.
            """
            # 使用MySQL或MariaDB时需要使用的语句:
            cursor.execute("""
                SELECT CONCAT(vend_name, TRIM('  (  '), vend_country, RTRIM(')  '))
                AS 'vend title'
                FROM Vendors
                ORDER BY vend_name;
            """)
            """
            注意: 别名
                别名的名字既可以是一个单词,也可用是一个字符串.如果是后者(譬如vend title),
                字符串应该括在引号中.虽然这种做法是合法的,但不建议这么去做.多单词的名字可读
                性高,不过会给客户端应用带来各种问题.因此,别名最常见的使用是将多个单词的列名
                重命名为一个单词的名字.
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'vend title': 'Bear Emporium(USA)'}
                {'vend title': 'Bears R Us(USA)'}
                {'vend title': 'Doll House Inc.(USA)'}
                {'vend title': 'Fun and Games(England)'}
                {'vend title': 'Furball Inc.(USA)'}
                {'vend title': 'Jouets et ours(France)'}
                """

    # 7.3 执行算术计算
    def test_arithmetic_calculation(self):
        """
        SQL算术操作符 +(加), -(减), *(乘), /(除)

        SELECT语句为测试,检验函数和计算提供了很好的方法.虽然SELECT通常用于从表中检索数据,
        但是省略了FROM子句后就是简单地访问和处理表达式,例如SELECT 3 * 2;将返回6,
        SELECT Trim('  ABC ');将返回ABC;SELECT Curdate();使用Curdate()函数返回当
        前日期和时间.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, quantity, item_price, quantity*item_price AS total
                FROM OrderItems
                WHERE order_num = 20008;
            """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_id': 'RGAN01', 'quantity': 5, 'item_price': Decimal('4.99'), 'total': Decimal('24.95')}
                {'prod_id': 'BR03', 'quantity': 5, 'item_price': Decimal('11.99'), 'total': Decimal('59.95')}
                {'prod_id': 'BNBG01', 'quantity': 10, 'item_price': Decimal('3.49'), 'total': Decimal('34.90')}
                {'prod_id': 'BNBG02', 'quantity': 10, 'item_price': Decimal('3.49'), 'total': Decimal('34.90')}
                {'prod_id': 'BNBG03', 'quantity': 10, 'item_price': Decimal('3.49'), 'total': Decimal('34.90')}
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. A common use for aliases is to rename table column fields in retrieved results
           (perhaps to match specific reporting or client needs). Write a SQL statement
           that retrieves vend_id, vend_name, vend_address, and vend_city from Vendors,
           renaming vend_name to vname, vend_city to vcity, and vend_address to vaddress.
           Sort the results by vendor name (you can use the original name or the renamed
           name).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_id, vend_name AS vname, vend_address AS vaddress, vend_city AS vcity
                FROM Vendors 
                ORDER BY vname;
                """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(vend_id='BRE02', vname='Bear Emporium', vaddress='500 Park Street', vcity='Anytown')
                Result(vend_id='BRS01', vname='Bears R Us', vaddress='123 Main Street', vcity='Bear Town')
                Result(vend_id='DLL01', vname='Doll House Inc.', vaddress='555 High Street', vcity='Dollsville')
                Result(vend_id='FNG01', vname='Fun and Games', vaddress='42 Galaxy Road', vcity='London')
                Result(vend_id='FRB01', vname='Furball Inc.', vaddress='1000 5th Avenue', vcity='New York')
                Result(vend_id='JTS01', vname='Jouets et ours', vaddress='1 Rue Amusement', vcity='Paris')
                """

    def test_exercise2(self):
        """
        2. Our example store is running a sale and all products are 10% off. Write a SQL
           statement that returns prod_id, prod_price, and sale_price from the Products
           table. sale_price is a calculated field that contains, well, the sale price.
           Here’s a hint, you can multiply by 0.9 to get 90% of the original value (and
           thus the 10% off price).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_id, prod_price, prod_price * 0.9 AS sale_price
                FROM Products;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_id='BNBG01', prod_price=Decimal('3.49'), sale_price=Decimal('3.141'))
                Result(prod_id='BNBG02', prod_price=Decimal('3.49'), sale_price=Decimal('3.141'))
                Result(prod_id='BNBG03', prod_price=Decimal('3.49'), sale_price=Decimal('3.141'))
                Result(prod_id='BR01', prod_price=Decimal('5.99'), sale_price=Decimal('5.391'))
                Result(prod_id='BR02', prod_price=Decimal('8.99'), sale_price=Decimal('8.091'))
                Result(prod_id='BR03', prod_price=Decimal('11.99'), sale_price=Decimal('10.791'))
                Result(prod_id='RGAN01', prod_price=Decimal('4.99'), sale_price=Decimal('4.491'))
                Result(prod_id='RYL01', prod_price=Decimal('9.49'), sale_price=Decimal('8.541'))
                Result(prod_id='RYL02', prod_price=Decimal('9.49'), sale_price=Decimal('8.541'))
                """
