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

    # 11.1
    """
    现在得到了订购物品RGAN01的所有顾客的ID。下一步是检索这些顾客ID的顾客倍息。检索两列
    的SQL语句为：
    """

    # 11.2利用子查询进行过滤
    def test_subquery_filtering(self):
        """
        本教程使用的数据库表都是关系表(关于每个表及关系的描述，请参阅create_table.models)。
        订单存储在两个表中。每个订单包含订单编号、客户ID、订单日期，在Orders表中存储为一行。
        各订单的物品存储在相关的OrderItems表中。Orders表不存储顾客信息，只存储顾客ID。顾客的
        实际信息存储在Customers表中。现在假如需要列出订购物品RGAN01的所有顾客，应该怎样检索？
        下面列出具体的步骤。
            (1) 检索包含物品RGAN01的所有订单的编号。
            (2) 检索具有前一步骤列出的订单编号的所有顾客的ID。
            (3) 检索前一步骤返回的所有顾客ID的顾客信息。
        上述每个步骤都可以单独作为一个查询来执行。可以把一条SELECT语句返回的结果用于另一条
        SELECT语句的WHERE子句。也可以使用子查询来把3个查询组合成一条语句。第一条SELECT语句的
        含义很明确，它对proc_id为RGAN01的所有订单物品，检索其order_num列。输出列出了两个包含
        此物品的订单：
        """
        """
        # SELECT order_num FROM orderitems WHERE prod_id='RGAN01'
        # SELECT cust_id FROM orders WHERE order_num IN (20007,20008)
        分析 ▼
            在SELECT语句中，子查询总是从内向外处理。在处理上面的SELECT语句时，DBMS实际上执行
            了两个操作。首先，它执行下面的查询：
            SELECT order_num FROM orderitems WHERE prod_id='RGAN01'
            此查询返回两个订单号：20007和20008。然后，这两个值以IN操作符,要求的逗号分隔的格式
            传递给外部查询的WHERE子句。外部查询变成: 
            SELECT cust_id FROM orders WHERE order_num IN (20007,20008)
            可以看到，输出是正确的，与前面硬编码WHERE子句所返回的值相同。
        """
        with connection.cursor() as cursor:
            """
            分析 ▼
                为了执行上述SELECT语句，DBMS实际上必须执行三条SELECT语句。最里边的子查询返回订单号
                列表，此列表用于其外面的子查询的WHERE子句。外面的子查询返回顾客ID列表，此顾客ID列表
                用于最外层查询的WHERE子句。最外层查询返回所需的数据。▼
            """
            cursor.execute("""
                SELECT cust_name, cust_contact
                FROM Customers
                WHERE cust_id IN (
                    SELECT cust_id
                    FROM Orders
                    WHERE order_num IN (
                        SELECT order_num
                        FROM OrderItems
                        WHERE prod_id = 'RGAN01'
                    )
                );
                """)
            """
            可见，在WHERE子句中使用子查询能够编写出功能很强且很灵活的SQL语句。对于能嵌套的子查询
            的数目没有限制，不过在实际使用时由于性能的限制，不能嵌套太多的子查询。
            
            提示：格式化SQL
                包含子查询的SELECT语句难以阅读和调试，它们在较为复杂时更是如此如上所示，把子查询分
                解为多行并进行适当的缩进，能极大地简化子查询的使用。顺便一提，这就是颜色编码起作用的
                地方，好的DBMS客户端正是出于这个原因使用了颜色代码SQL。
            注意：只能是单列
                作为子查询的SELECT语句只能查询单个列。企图检索多个列将返回错误
            注意：子查询和性能
                这里给出的代码有效，并且获得了所需的结果。但是，使用子查询并  
                不总是执行这类数据检索的最有效方法。更多的论述，请参阅第12  
                课，其中将再次给出这个例子。
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_name': 'Fun4All', 'cust_contact': 'Denise L. Stephens'}
                {'cust_name': 'The Toy Store', 'cust_contact': 'Kim Howard'}
                """

            print("=" * 60)
            """使用子查询获取平均价格, 再过滤大于平均价格的数据."""
            cursor.execute("""
                SELECT prod_id, (quantity * item_price) AS price
                FROM OrderItems
                WHERE (quantity * item_price) >= (
                    SELECT AVG(quantity * item_price)
                    FROM OrderItems
                );
                """)
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'prod_id': 'BR01', 'price': Decimal('549.00')}
                {'prod_id': 'BR03', 'price': Decimal('1099.00')}
                {'prod_id': 'BR03', 'price': Decimal('574.50')}
                {'prod_id': 'BNBG01', 'price': Decimal('622.50')}
                {'prod_id': 'BNBG02', 'price': Decimal('622.50')}
                {'prod_id': 'BNBG03', 'price': Decimal('622.50')}
                """

    # 11.3 作为计算字段使用子查询
    def test_count_func(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name, cust_state, (
                    SELECT COUNT(*)
                    FROM Orders
                    WHERE Orders.cust_id = Customers.cust_id
                ) AS orders
                FROM Customers
                ORDER BY cust_name;
                """)
            """
            分析 ▼
                这条SELECT语句对Customers表中每个顾客返回三列：cust_name、cust_state和orders。
                orders是一个计算字段，它是由圆括号中的子査询建立的。该子查询对检索出的每个顾客执行一
                次。在此例中，该子查询执行了5次，因为检索出了5个顾客。
                
                子查询中的WHERE子句与前面使用的WHERE子句稍有不同，因为它使用了完全限定列名，而不只是
                列名(cust_id)。它指定表名和列名(Orders.cust_id和Customers.cust_id)。下面的
                WHERE子句告诉SQL，比较Orders表中的cust_id和当前正从Customers表中检索的cust_id:
                
                WHERE Orders.cust_id = Customers.cust_id
            """
            for result in dictfetchall(cursor):  # 读取所有
                print(result)
                """
                {'cust_name': 'Fun4All', 'cust_state': 'IN', 'orders': 1}
                {'cust_name': 'Fun4All', 'cust_state': 'AZ', 'orders': 1}
                {'cust_name': 'Kids Place', 'cust_state': 'OH', 'orders': 0}
                {'cust_name': 'The Toy Store', 'cust_state': 'IL', 'orders': 1}
                {'cust_name': 'Village Toys', 'cust_state': 'MI', 'orders': 2}
                """
            """
            分析 ▼
                WHERE Orders.cust_id = Customers.cust_id
                用一个句点分隔表名和列名，在有可能混淆列名时必须使用这种语法。在这个例子中，有两个
                cust_id列：一个在Customers中，另一个在Orders中。如果不采用完全限定列名，DBMS会认为
                要对Orders表中的cust_id自身进行比较。
                因为SELECT C0UNT(*) FROM Orders WHERE cust_id = cust_id总是返冋Orders表中订
                单的总数，而这个结果不是我们想要的.
            """

    # 课后练习
    def test_exercise1(self):
        """
        1. Using a subquery, return a list of customers who bought items priced 10 or more.
           You’ll want to use the OrderItems table to find the matching order numbers
           (order_num), and then the Orders table to retrieve the customer id (cust_id) for
           those matched orders.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_name
                FROM Customers
                WHERE cust_id IN (
                    SELECT cust_id
                    FROM Orders
                    WHERE order_num IN  (
                        SELECT order_num
                        FROM OrderItems
                        WHERE item_price >= 10
                    )
                );
                """)
            for result in namedtuplefetchall(cursor): # 读取所有
                print(result)
                """
                Result(cust_name='Village Toys')
                Result(cust_name='Fun4All')
                Result(cust_name='Fun4All')
                Result(cust_name='The Toy Store')
                """

    def test_exercise2(self):
        """
        2. You need to know the dates when product BR01 was ordered. Write a SQL statement
           that uses a subquery to determine which orders (in OrderItems) purchased prod_id
           BR01, and then returns customer id (cust_id) and order date (order_date) for
           each from the Orders table. Sort the results by order date.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_id, order_date
                FROM Orders
                WHERE order_num IN (
                    SELECT order_num
                    FROM OrderItems
                    WHERE prod_id = 'BR01'
                )
                ORDER BY order_date
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000003', order_date=datetime.datetime(2020, 1, 12, 0, 0))
                Result(cust_id='1000000001', order_date=datetime.datetime(2020, 5, 1, 0, 0))
                """

    def test_exercise3(self):
        """
        3. Now let’s make it a bit more challenging. Update the previous challenge to return
           the customer email (cust_email in the Customers table) for any customers who
           purchased item with a prod_id of BR01. Hint, this involves the SELECT statement,
           the innermost one returning order_num from OrderItems, and the middle one returning
           cust_id from Orders.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_email
                FROM Customers
                WHERE cust_id IN (
                    SELECT cust_id
                    FROM Orders
                    WHERE order_num IN (
                        SELECT order_num
                        FROM OrderItems
                        WHERE prod_id = 'BR01'
                    )
                )
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_email='sales@villagetoys.com')
                Result(cust_email='jjones@fun4all.com')
                """

    def test_exercise4(self):
        """
        4. We need a list of customer ids with the total amount they have ordered. Write a SQL
           statement to return customer id (cust_id in Orders table) and total_ordered using a
           subquery to return the total of orders for each customer. Sort the results by amount
           spent from greatest to the least. Hint, you’ve used the SUM() to calculate order
           totals previously.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_id, (
                    SELECT SUM(quantity * item_price)
                    FROM OrderItems
                    WHERE order_num IN (
                        SELECT order_num
                        FROM Orders
                        WHERE Orders.cust_id = Customers.cust_id
                    )
                ) AS total_ordered
                FROM Customers;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000001', total_ordered=Decimal('3515.50'))
                Result(cust_id='1000000002', total_ordered=None)
                Result(cust_id='1000000003', total_ordered=Decimal('329.60'))
                Result(cust_id='1000000004', total_ordered=Decimal('1696.00'))
                Result(cust_id='1000000005', total_ordered=Decimal('189.60'))
                """

            """
            # 下面为书中答案, 但本人认为不正确.
            SELECT cust_id,
                   (SELECT SUM(item_price*quantity) 
                    FROM OrderItems
                    WHERE Orders.order_num = OrderItems.order_num) AS total_ordered
            FROM Orders
            ORDER BY total_ordered DESC;
            """

    def test_exercise5(self):
        """
        5. One more. Write a SQL statement that retrieves all product names (prod_name) from the
           Products table, along with a calculated named quant_sold containing the total number
           of this item sold (retrieved using a subquery and a SUM(quantity) on the OrderItems
           table).
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT prod_name, (
                    SELECT SUM(quantity)
                    FROM OrderItems
                    WHERE OrderItems.prod_id = Products.prod_id
                ) AS quant_sold
                FROM Products
                ORDER BY quant_sold DESC;
                """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(prod_name='Fish bean bag toy', quant_sold=Decimal('360'))
                Result(prod_name='Bird bean bag toy', quant_sold=Decimal('360'))
                Result(prod_name='Rabbit bean bag toy', quant_sold=Decimal('360'))
                Result(prod_name='18 inch teddy bear', quant_sold=Decimal('165'))
                Result(prod_name='8 inch teddy bear', quant_sold=Decimal('120'))
                Result(prod_name='Raggedy Ann', quant_sold=Decimal('55'))
                Result(prod_name='12 inch teddy bear', quant_sold=Decimal('10'))
                Result(prod_name='King doll', quant_sold=None)
                Result(prod_name='Queen doll', quant_sold=None)
                """