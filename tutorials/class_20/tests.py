#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'


from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *
from utils.functions import namedtuplefetchall, dictfetchall, dictfetchone


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

    # 12.7.2 创建触发器(MySQL基础教程)
    def test_create_trigger(self):
        """
        触发器被触发的时机包括以下两种.
            触发器被触发的时机
                BEFORE: 在对表进行处理之前触发
                AFTER : 在对表进行处理之后触发

        对表进行处理之前的列值和对表进行处理之后的列值, 可以像下面这样通过"OLD.列名" "NEW.列名"获得.
            列值
                OLD.列名: 对表进行处理之前的列值
                NEW.列名: 对表进行处理之后的列值

        执行INSERT, UPDATE和DELETE命令之前的列值可以通过"OLD.列名"获得,执行这些命令之后的列值可以
        通过"NEW.列值"获得.

        但是, 根据命令的不同, 有的列值可以取出来, 有的列值不能取出来. ⭕表示可以取出来的列值.
        命令      执行前(OLD.列名) 使用BEFORE     执行后(NEW.列名) 使用AFTER
        INSERT           ❌                               ⭕
        DELETE           ⭕                               ❌
        UPDATE           ⭕                               ⭕
        """

        # 1: 复制表的结构做为触发器记录表备用
        # 2: 创建触发器
        # 3: 删除表数据
        # 4: 查看原表和触发器记录表的数据
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE OrderItemsCopy LIKE OrderItems;
            """)
            cursor.execute("""
                # tr1为自定义触发器名字
                CREATE TRIGGER tr1 BEFORE DELETE ON OrderItems FOR EACH ROW 
                BEGIN 
                INSERT INTO OrderItemsCopy (
                    id,
                    order_num,
                    prod_id, 
                    order_item, 
                    quantity,
                    item_price
                )
                VALUES (
                    OLD.id,
                    OLD.order_num,
                    OLD.prod_id, 
                    OLD.order_item, 
                    OLD.quantity,
                    OLD.item_price
                );
                END;
            """)
            cursor.execute("DELETE FROM OrderItems WHERE quantity>0")

            cursor.execute("SELECT * FROM OrderItems")
            print("OrderItems")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)

            print("OrderItemsCopy")
            cursor.execute("SELECT id, order_num, item_price FROM OrderItemsCopy")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'id': 1, 'order_num': 20005, 'item_price': Decimal('5.49')}
                {'id': 2, 'order_num': 20005, 'item_price': Decimal('10.99')}
                {'id': 3, 'order_num': 20006, 'item_price': Decimal('5.99')}
                {'id': 4, 'order_num': 20006, 'item_price': Decimal('8.99')}
                {'id': 5, 'order_num': 20006, 'item_price': Decimal('11.99')}
                {'id': 6, 'order_num': 20007, 'item_price': Decimal('11.49')}
                {'id': 7, 'order_num': 20007, 'item_price': Decimal('2.99')}
                {'id': 8, 'order_num': 20007, 'item_price': Decimal('2.99')}
                {'id': 9, 'order_num': 20007, 'item_price': Decimal('2.99')}
                {'id': 10, 'order_num': 20007, 'item_price': Decimal('4.49')}
                {'id': 11, 'order_num': 20008, 'item_price': Decimal('4.99')}
                {'id': 12, 'order_num': 20008, 'item_price': Decimal('11.99')}
                {'id': 13, 'order_num': 20008, 'item_price': Decimal('3.49')}
                {'id': 14, 'order_num': 20008, 'item_price': Decimal('3.49')}
                {'id': 15, 'order_num': 20008, 'item_price': Decimal('3.49')}
                {'id': 16, 'order_num': 20009, 'item_price': Decimal('2.49')}
                {'id': 17, 'order_num': 20009, 'item_price': Decimal('2.49')}
                {'id': 18, 'order_num': 20009, 'item_price': Decimal('2.49')}
                """

            # 12.8.1 确认设置的触发器
            cursor.execute("SHOW TRIGGERS;")
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {
                    'Trigger': 'tr1', 
                    'Event': 'DELETE', 
                    'Table': 'OrderItems', 
                    'Statement': 'BEGIN \n                '
                                 'INSERT INTO OrderItemsCopy (\n                    '
                                     'id,\n                    '
                                     'order_num,\n                    '
                                     'prod_id, \n                    '
                                     'order_item, \n                    '
                                     'quantity,\n                    '
                                     'item_price\n                '
                                 ')\n                '
                                 'VALUES (\n                    '
                                     'OLD.id,\n                    '
                                     'OLD.order_num,\n                    '
                                     'OLD.prod_id, \n                    '
                                     'OLD.order_item, \n                    '
                                     'OLD.quantity,\n                    '
                                     'OLD.item_price\n                '
                                 ');\n                '
                                 'END', 
                    'Timing': 'BEFORE', 
                    'Created': datetime.datetime(2020, 11, 14, 19, 54, 48, 340000), 
                    'sql_mode': 'STRICT_TRANS_TABLES', 
                    'Definer': 'root@%', 
                    'character_set_client': 'utf8mb4', 
                    'collation_connection': 'utf8mb4_general_ci', 
                    'Database Collation': 'utf8mb4_unicode_ci'
                }
                """

            # 12.8.2 删除触发器
            cursor.execute("DROP TRIGGER tr1;")


