#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'

from django.test import TestCase
from django.db import connection

from tutorials.create_table.models import *


# Create your tests here.


class TestHealthFile(TestCase):
    def setUp(self):
        cursor = connection.cursor()

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

    def test_customers(self):
        for i in Customers.objects.all():
            print(i.to_dict())

        for i in Vendors.objects.all():
            print(i.to_dict())

        for i in Orders.objects.all():
            print(i.to_dict())

        for i in OrderItems.objects.all():
            print(i.to_dict())

        for i in Products.objects.all():
            print(i.to_dict())