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
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000001', 'Village Toys', '200 Maple Lane', 'Detroit', 'MI', '44444', 'USA', 'John Smith', 'sales@villagetoys.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000002', 'Kids Place', '333 South Lake Drive', 'Columbus', 'OH', '43333', 'USA', 'Michelle Green');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000003', 'Fun4All', '1 Sunny Place', 'Muncie', 'IN', '42222', 'USA', 'Jim Jones', 'jjones@fun4all.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
            VALUES('1000000004', 'Fun4All', '829 Riverside Drive', 'Phoenix', 'AZ', '88888', 'USA', 'Denise L. Stephens', 'dstephens@fun4all.com');"
            )
            cursor.execute(
                "INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact) \
            VALUES('1000000005', 'The Toy Store', '4545 53rd Street', 'Chicago', 'IL', '54545', 'USA', 'Kim Howard');"
            )

            # Populate Vendors table
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRS01','Bears R Us','123 Main Street','Bear Town','MI','44444', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('BRE02','Bear Emporium','500 Park Street','Anytown','OH','44333', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('DLL01','Doll House Inc.','555 High Street','Dollsville','CA','99999', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FRB01','Furball Inc.','1000 5th Avenue','New York','NY','11111', 'USA');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('FNG01','Fun and Games','42 Galaxy Road','London', NULL,'N16 6PS', 'England');"
            )
            cursor.execute(
                "INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city, vend_state, vend_zip, vend_country) \
            VALUES('JTS01','Jouets et ours','1 Rue Amusement','Paris', NULL,'45678', 'France');"
            )

            # Populate Products table
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR01', 'BRS01', '8 inch teddy bear', 5.99, '8 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR02', 'BRS01', '12 inch teddy bear', 8.99, '12 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BR03', 'BRS01', '18 inch teddy bear', 11.99, '18 inch teddy bear, comes with cap and jacket');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG01', 'DLL01', 'Fish bean bag toy', 3.49, 'Fish bean bag toy, complete with bean bag worms with which to feed it');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG02', 'DLL01', 'Bird bean bag toy', 3.49, 'Bird bean bag toy, eggs are not included');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('BNBG03', 'DLL01', 'Rabbit bean bag toy', 3.49, 'Rabbit bean bag toy, comes with bean bag carrots');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RGAN01', 'DLL01', 'Raggedy Ann', 4.99, '18 inch Raggedy Ann doll');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL01', 'FNG01', 'King doll', 9.49, '12 inch king doll with royal garments and crown');"
            )
            cursor.execute(
                "INSERT INTO Products(prod_id, vend_id, prod_name, prod_price, prod_desc) \
            VALUES('RYL02', 'FNG01', 'Queen doll', 9.49, '12 inch queen doll with royal garments and crown');"
            )

            # Populate Orders table
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20005, '2020-05-01', '1000000001');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20006, '2020-01-12', '1000000003');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20007, '2020-01-30', '1000000004');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20008, '2020-02-03', '1000000005');"
            )
            cursor.execute(
                "INSERT INTO Orders(order_num, order_date, cust_id) \
            VALUES(20009, '2020-02-08', '1000000001');"
            )

            # Populate OrderItems table
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 1, 'BR01', 100, 5.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20005, 2, 'BR03', 100, 10.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 1, 'BR01', 20, 5.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 2, 'BR02', 10, 8.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20006, 3, 'BR03', 10, 11.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 1, 'BR03', 50, 11.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 2, 'BNBG01', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 3, 'BNBG02', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 4, 'BNBG03', 100, 2.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20007, 5, 'RGAN01', 50, 4.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 1, 'RGAN01', 5, 4.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 2, 'BR03', 5, 11.99);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 3, 'BNBG01', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 4, 'BNBG02', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20008, 5, 'BNBG03', 10, 3.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 1, 'BNBG01', 250, 2.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 2, 'BNBG02', 250, 2.49);"
            )
            cursor.execute(
                "INSERT INTO OrderItems(order_num, order_item, prod_id, quantity, item_price) \
            VALUES(20009, 3, 'BNBG03', 250, 2.49);"
            )

    def tearDown(self):
        # Clean up run after every test method.
        Customers.objects.all().delete()
        Vendors.objects.all().delete()
        Orders.objects.all().delete()
        OrderItems.objects.all().delete()
        Products.objects.all().delete()

    # 16.1.1 更新指定数据某一个值
    def test_update_a_value(self):
        """
        注意：不要省略WHERE子句
            在使用UPDATE时一定要细心.因为稍不注意，就会更新表中的所有行。
        提示：UPDATE与安全
            在客户端/服务器的DBMS中，使用UPDATE语句可能需要特殊的安全权限。
            在你使用UPDATE前，应该保证自己有足够的安全权限。
        """
        with connection.cursor() as cursor:

            cursor.execute("""
                UPDATE Customers
                SET cust_email = 'kim@thetoystore.com'
                WHERE cust_id = 1000000005
            """)
            """
            UPDATE语句总是以要更新的表名开始。在这个例子中，要更新的表名为 
            Customers。SET命令用来将新值赋给被更新的列。在这里，SET子句设 
            置cust_email列为指定的值：
            SET cust_email = 'kim@thetoystore.com'
            UPDATE语句以WHERE子句结束，它告诉DBMS更新哪一行。没有WHERE 
            子句，DBMS将会用这个电子邮件地址更新Customers表中的所有行， 
            这不是我们希望的。
            """
            print(Customers.objects.get(cust_id=1000000005).to_dict())
            """
            {
                "cust_id": "1000000005",
                "cust_name": "The Toy Store",
                "cust_address": "4545 53rd Street",
                "cust_city": "Chicago",
                "cust_state": "IL",
                "cust_zip": "54545",
                "cust_country": "USA",
                "cust_contact": "Kim Howard",
                "cust_email": "kim@thetoystore.com",
            }            
            """


    # 16.1.2 更新指定数据多个值
    def test_update_multiple_values(self):
        """
        提示：在UPDATE语句中使用子查询
             UPDATE语句中可以使用子查询，使得能用SELECT语句检索出的数据更新列数据。
        提示：FROM关键字
             有的SQL实现支持在UPDATE语句中使用FROM子句，用一个表的数据更新另一个表
             的行。如想知道你的DBMS是否支持这个特性，请参阅它的文档.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE Customers
                SET cust_email = 'sam@toyland.com', cust_contact = 'Sam Roberts'
                WHERE cust_id = 1000000005;
            """)
            print(Customers.objects.get(cust_id=1000000005).to_dict())

    # 16.1.3 更新指定数据某个值为空值
    def test_update_to_null(self):
        with connection.cursor() as cursor:
            """
            要删除某个列的值，可设置它为NULL (假如表定义允许NULL值)。如下
            """
            cursor.execute("""
                UPDATE Customers
                SET cust_email = NULL
                WHERE cust_id = 1000000005;
            """)
            """
            其中NULL用来去除cust_email列中的值。这与保存空字符串很不同
            (空字符串用''表示，是一个值)，而NULL表示没有值。
            """
            print(Customers.objects.get(cust_id=1000000005).to_dict())

    # 16.2 删除数据
    def test_delete_date(self):
        """
        注意：不要省略WHERE子句
            在使用DELETE时一定要细心.因为稍不注意，就会删除表中的所有行。
        提示：DELETE与安全
            在客户端/服务器的DBMS中，使用DELETE语句可能需要特殊的安全权限。
            在你使用DELETE前，应该保证自己有足够的安全权限。
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE 
                FROM OrderItems
                WHERE order_num = 20005;
            """)
            self.assertFalse(OrderItems.objects.filter(order_num=20005).exists())

        """
        提示：友好的外键
            第12章介绍了联结，简单联结两个表只需要这两个表中的公用字段。
            也可以让DBMS通过使用外键来严格实施关系。存在外键时，DBMS
            使用它们实施引用完整性。例如要向Products表中插入一个新产品，
            DBMS不允许通过未知的供应商id插入它，因为vend_id列是作为外
            键连接到vendors表的。那么，这与DELETE有什么关系呢？使用外
            键确保引用完整性的一个好处是，DBMS通常可以防止删除某个关系需
            要用到的行.例如，要从Products表中删除一个产品，而这个产品用
            在OrderItems的已有订单中，那么DELETE语句将抛出错误并中止。
            这是总要定义外键的另一个理由。
        提示：FROM关键字
            在某些SQL实现中，跟在DELETE后的关键字FROM是可选的。但是即使
            不需要，也最好提供这个关键字。这样做将保证SQL代码在DBMS之间可
            移植。

        DELETE不需要列名或通配符。DELETE删除整行而不是删除列。要删除 
        指定的列，请使用UPDATE语句。
        
        说明：删除表的内容而不是表
            DELETE语句从表中删除行，甚至是删除表中所有行。但是，DELETE 
            不删除表本身。
        提示：更快的删除
            如果想从表中删除所有行，不要使用DELETE。可使用TRUNCATE TABLE 
            语句，它完成相同的工作，而速度更快（因为不记录数据的变动)。
        """

    # 16.3 更新和删除的指导原则
    """
    上面使用的UPDATE和DELETE语句都有WHERE子句，这样做的理由
    很充分。如果省略了WHERE子句，则UPDATE或DELETE将被应用到表
    中所有的行。换句话说，如执行UPDATE而不带WHERE子句,则表中
    每一行都将用新值更新。类似地，如果执行DELETE语句而不带WHERE
    子句，表的所有数据都将被删除。
    
    下面是许多SQL程序员使用UPDATE或DELETE时所遵循的重要原则。
    
    - 除非确实打算更新和删除每一行，否则绝对不要使用不带WHERE子句
      的UPDATE或DELETE语句。
    - 保证每个表都有主键(如果忘记这个内容，请参阅第12章)，尽可能
      像WHERE子句那样使用它(可以指定各主键、多个值或值的范围) 。
    
    - 在UPDATE或DELETE语句使用WHERE子句前，应该先用SELECT进
      行测试，保证它过滤的是正确的记录，以防编写的WHERE子句不正确。
    - 使用强制实施引用完整性的数据库(关于这个内容，请参阅第12章)，
      这样DBMS将不允许删除其数据与其他表相关联的行。
    - 有的DBMS允许数据库管理员施加约束，防止执行不带WHERE子句
      的UPDATE或DELETE语句。如果所采用的DBMS支持这个特性，应
      该使用它。
    若是SQL没有撤销(undo) 按钮， 应该非常小心地使用UPDATE和DELETE，
    否则你会发现自己更新或删除了错误的数据。
    """

    # 课后练习
    def test_exercise1(self):
        """
        1. USA State abbreviations should always be in upper case. Write a SQL statement
           to update all USA addresses, both vendor states (vend_state in Vendors) and
           customer states (cust_state in Customers) so that they are upper case.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE Vendors
                SET vend_state=UPPER(vend_state);
            """)
            for i in Vendors.objects.all():
                print(i.vend_state)

            cursor.execute("""
                UPDATE Customers
                SET cust_state=UPPER(cust_state);
            """)
            for i in Customers.objects.all():
                print(i.cust_state)

    def test_exercise2(self):
        """
        2. In Lesson 15 Challenge 1 I asked you to add yourself to the Customers table.
           Now delete yourself. Make sure to use a WHERE clause (and test it with a
           SELECT before using it in DELETE) or you’ll delete all customers!
        """
        with connection.cursor() as cursor:
            cust: Customers = Customers.objects.create(
                cust_id=1000000006,
                cust_name='Toy Land',
                cust_address='123 Any Street',
                cust_city='New York',
                cust_state='NY',
                cust_zip='11111',
                cust_country='USA',
            )
            cursor.execute(f"""
                DELETE
                FROM Customers
                WHERE cust_id = {cust.cust_id}
            """)
            self.assertFalse(Customers.objects.filter(cust_id=cust.cust_id).exists())
