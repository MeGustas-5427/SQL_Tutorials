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

    """
    MyISAM:  拥有较高的插入、查询速度，但不支持事务。
    InnoDB:  事务型数据库的首选引擎，支持事务安全表（ACID），支持行锁定和外键. 默认的MySQL引擎。
    MEMORY:  存储引擎将表中的数据存储到内存中，未查询和引用其他表数据提供快速访问。如果只是临时存放数据，数据量不大，
             并且不需要较高的数据安全性，可以选择将数据保存在内存中的Memory引擎，MySQL中使用该引擎作为临时表，存放
             查询的中间结果。数据的处理速度很快但是安全性不高。
    Archive: 如果只有INSERT和SELECT操作，可以选择Archive，Archive支持高并发的插入操作，但是本身不是事务安全的。
             Archive非常适合存储归档数据，如记录日志信息可以使用Archive
    """

    # 13.2.1 确认存储引擎(MySQL基础教程)
    def test_inquiry_engine(self):
        with connection.cursor() as cursor:
            cursor.execute("SHOW CREATE TABLE OrderItems")
            result = dictfetchone(cursor)
            print(result)
            # ENGINE=xxxx 的部分确认存储引擎.
            """
            {
                "Table": "OrderItems",
                "Create Table": 
                    "CREATE TABLE `OrderItems` (\n  "
                    "`id` int NOT NULL AUTO_INCREMENT,\n  "
                    "`order_item` int NOT NULL,\n  "
                    "`quantity` int NOT NULL,\n  "
                    "`item_price` decimal(8,2) NOT NULL,\n  "
                    "`order_num` int NOT NULL,\n  "
                    "`prod_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,\n  "
                    "PRIMARY KEY (`id`),\n  "
                    "UNIQUE KEY `OrderItems_order_num_order_item_c405df47_uniq` (`order_num`,`order_item`),\n  "
                    "KEY `OrderItems_prod_id_9bdcba25_fk_Products_prod_id` (`prod_id`),\n  "
                    "CONSTRAINT `OrderItems_order_num_ce305812_fk_Orders_order_num` "
                    "FOREIGN KEY (`order_num`) "
                    "REFERENCES `Orders` (`order_num`),\n  "
                    "CONSTRAINT `OrderItems_prod_id_9bdcba25_fk_Products_prod_id` "
                    "FOREIGN KEY (`prod_id`) "
                    "REFERENCES `Products` (`prod_id`)\n) "
                    "ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci",
            }
            """

    # 13.2.2 修改存储引擎(MySQL基础教程)
    def test_update_engine(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (
                    prod_id CHAR(10) NOT NULL,
                    vend_id CHAR(10) NOT NULL,
                    prod_name CHAR(254) NOT NULL,
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000) NOT NULL DEFAULT 'balabala'
                );
            """)
            cursor.execute("ALTER TABLE TestTable ENGINE=MEMORY;")
            cursor.execute("SHOW CREATE TABLE TestTable")
            result = dictfetchone(cursor)
            print(result)
            """
            {
                'Table': 'TestTable', 
                'Create Table': 
                    "CREATE TABLE `TestTable` (\n  "
                        "`prod_id` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,\n  "
                        "`vend_id` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,\n  "
                        "`prod_name` char(254) COLLATE utf8mb4_unicode_ci NOT NULL,\n  "
                        "`prod_price` decimal(8,2) NOT NULL,\n  "
                        "`prod_desc` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'balabala'\n"
                    ") ENGINE=MEMORY DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"
            }
            """

    # 13.4.2 开启事务(MySQL基础教程)
    def test_start_transaction(self):
        with connection.cursor() as cursor:
            # 首次删除并回滚
            cursor.execute("START TRANSACTION;")  # 开启事务(cursor.execute("BEGIN;")也可以开启事务)
            cursor.execute("DELETE FROM OrderItems WHERE quantity>0;")
            cursor.execute("SELECT id FROM OrderItems;")
            print("1:DELETE==>")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
            cursor.execute("ROLLBACK;")  # 回滚复原
            print("1:ROLLBACK==>")
            cursor.execute("SELECT id FROM OrderItems;")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)

            # 再次删除并回滚
            cursor.execute("DELETE FROM OrderItems WHERE quantity>0;")
            cursor.execute("SELECT id FROM OrderItems;")
            print("2:DELETE==>")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
            cursor.execute("ROLLBACK;")  # 回滚复原
            print("2:ROLLBACK==>")
            cursor.execute("SELECT id FROM OrderItems;")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)

            # 再次删除并提交(提交后即使回滚也复原不了数据)
            cursor.execute("DELETE FROM OrderItems WHERE quantity>0;")
            cursor.execute("SELECT id FROM OrderItems;")
            print("3:DELETE==>")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
            cursor.execute("COMMIT;")  # 提交
            cursor.execute("ROLLBACK;")  # 回滚复原
            print("3:ROLLBACK==>")
            cursor.execute("SELECT id FROM OrderItems;")
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)