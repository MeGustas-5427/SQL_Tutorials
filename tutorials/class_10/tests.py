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

    # 10.2 创建分组(GROUP BY)
    def test_create_grouping(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_id, COUNT(*) AS num_prods
                FROM Products 
                GROUP BY vend_id;
            """)
            """
            上面的SELECT语句指定了两个列：vend_id包含产品供应商的ID，
            num_prods为计算字段（用COUNT(*)函数建立）。GROUP BY子句指示
            DBMS按vend_id排序并分组数据。这就会对每个vend_id而不是整个
            表计算num_prods一次。从输出中可以看到，供应商BRS01有3个产
            品，供应商DLL01有4个产品，而供应商FNG01有2个产品。
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_id='BRS01', num_prods=3)
                Result(vend_id='DLL01', num_prods=4)
                Result(vend_id='FNG01', num_prods=2)
                """
            """
            在使用GROUP BY子句前，需要知道—些重要的规定。
                □	GROUP BY子句可以包含任意数目的列，因而可以对分组进行嵌套，
                    更细致地进行数据分组。
                □   如果在GROUP BY子句中嵌套了分组，数据将在最后指定的分组上进
                    行汇总。换句话说，在建立分组时，指定的所有列都一起计算（所以
                    不能从个别的列取回数据)。
                □	GROUP BY子句中列出的每一列都必须是检索列或有效的表达式（但
                    不能是聚集函数)。如果在SELECT中使用表达式，则必须在GROUP BY
                    子句中指定相同的表达式。不能使用别名。
                □   大多数SQL实现不允许GROUP BY列带有长度可变的数据类型（如文
                    本或备注型字段)。
                □   除聚集计算语句外，SELECT语句中的每一列都必须在GROUP BY子句
                    中给出。
                □   如果分组列中包含具有NULL值的行，则NULL将作为一个分组返回。
                    如果列中有多行NULL值，它们将分为一组。
                □   GROUP BY子句必须出现在WHERE子句之后，ORDER BY子句之前。

            提示: ALL子句
                Microsoft SQL Server等有些SQL实现在GR0UP BY中支持可选的ALL
                子句。这个子句可用来返回所有分组，即使是没有匹配行的分组也返回(在此
                情况下，聚集将返回NULL)。具体的DBMS是否支持ALL，查相应文档.

            注意:通过相对位置指定列
                有的SOL 实现允许根据SELECT 列表中的位置指定GROUP BY的列。譬如, 
                GROUP BY 2, 1 可表示按选择的第二个列分组,然后再按第一个列分组。
                虽然这种速记语法很方便,但并非所有SQL实现都支持,并且使用它容易在编
                辑SQL语句时出错。
            """

    # 10.3 过滤分组(HAVING子句)
    def test_having(self):
        """
        除了能用GROUP BY分组数据外，SQL还允许过滤分组，规定包括哪些
        分组，排除哪些分组。例如，你可能想要列出至少有两个订单的所有顾
        客。为此，必须基于完整的分组而不是个别的行进行过滤。

        我们已经看到了 WHERE子句的作用（第4课提及)。但是，在这个例子
        中WHERE不能完成任务，因为WHERE过滤指定的是行而不是分组。事实
        上，WHERE没有分组的概念。

        那么，不使用WHERE使用什么呢？ SQL为此提供了另一个子句，就是
        HAVING子句。HAVING非常类似于WHERE。事实上，目前为止所学过的
        所有类型的WHERE子句都可以用HAVING来替代。唯一的差别是，WHERE
        过滤行，而HAVING过滤分组。
        """

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cust_id, COUNT(*) AS orders
                FROM Orders
                GROUP BY cust_id
                HAVING COUNT(*) >= 2;
            """)
            """
            提示：HAVING支持所有WHERE操作符
                我们学习了 WHERE子句的条件（包括通配符条件和带多个操作
                符的子句）。学过的这些有关WHERE的所有技术和选项都适用
                于HAVING。它们的句法是相同的，只是关键字有差别。
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(cust_id='1000000001', orders=2)
                """

            print("=" * 60)

            cursor.execute("""
                SELECT vend_id, COUNT(*) AS num_prods
                FROM Products
                WHERE prod_price >= 4
                GROUP BY vend_id
                HAVING COUNT(*) >= 2;
            """)
            """
            说明：HAVING和WHERE的差别
                这里有另一种理解方法，WHERE在数据分组前进行过滤，HAVING在数 
                据分组后进行过滤。这是一个重要的区别，WHERE排除的行不包括在 
                分组中。这可能会改变计算值，从而影响HAVING子句中基于这些值 
                过滤掉的分组。    
            说明：使用HAVING和WHERE
                HAVING与WHERE非常类似，如果不指定GROUP BY，则大多数DBMS
                会同等对待它们。不过，你自己要能区分这一点。使用HAVING时应 
                该结合GROUP BY子句，而WHERE子句用于标准的行级过滤.
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_id='BRS01', num_prods=3)
                Result(vend_id='FNG01', num_prods=2)
                """

    # 10.4 分组和排序
    def test_group_by_and_order_py(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, COUNT(*) AS items
                FROM OrderItems 
                GROUP BY order_num
                HAVING COUNT(*) >= 3
                ORDER BY 2, 1;
            """)
            """
            提示: 不要忘记ORDER BY
                 一般在使用GROUP BY子句时，应该也给出ORDER BY子句。这是保
                 数据正确排序的唯一方法。千万不要仅依赖GROUP BY排序数据。
            """
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20006, items=3)
                Result(order_num=20009, items=3)
                Result(order_num=20007, items=5)
                Result(order_num=20008, items=5)
                """

    # WITH ROLLUP(MYSQL)
    def test_with_rollup(self):
        """
        http://mysql.taobao.org/monthly/2019/08/08/
        通常情况下，我们不光需要这种最高层次的统计结果，也需要在更低的层次进行分析。
        比如说，某个order_num的某个order_item的总和，以及某个order_num的总和。
        为了达到这样的效果，我们可能需要对 Group By List 中的属性列进行调整，并
        重新执行查询语句得到我们需要的结果。但是 ROLLUP 功能使得我们可以仅通过一条
        查询语句实现上述效果
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, order_item, COUNT(*) AS items
                FROM OrderItems 
                GROUP BY order_num, order_item WITH ROLLUP;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, order_item=1, items=1)
                Result(order_num=20005, order_item=2, items=1)
                Result(order_num=20005, order_item=None, items=2)
                Result(order_num=20006, order_item=1, items=1)
                Result(order_num=20006, order_item=2, items=1)
                Result(order_num=20006, order_item=3, items=1)
                Result(order_num=20006, order_item=None, items=3)
                Result(order_num=20007, order_item=1, items=1)
                Result(order_num=20007, order_item=2, items=1)
                Result(order_num=20007, order_item=3, items=1)
                Result(order_num=20007, order_item=4, items=1)
                Result(order_num=20007, order_item=5, items=1)
                Result(order_num=20007, order_item=None, items=5)
                Result(order_num=20008, order_item=1, items=1)
                Result(order_num=20008, order_item=2, items=1)
                Result(order_num=20008, order_item=3, items=1)
                Result(order_num=20008, order_item=4, items=1)
                Result(order_num=20008, order_item=5, items=1)
                Result(order_num=20008, order_item=None, items=5)
                Result(order_num=20009, order_item=1, items=1)
                Result(order_num=20009, order_item=2, items=1)
                Result(order_num=20009, order_item=3, items=1)
                Result(order_num=20009, order_item=None, items=3)
                Result(order_num=None, order_item=None, items=18)
                """

    # 课后练习
    def test_exercise1(self):
        """
        1. The OrderItems table contains the individual items for each order.Write a
           SQL statement that returns the number of lines (as order_lines) for each
           order number (order_num) and sort the results buy order_lines.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, COUNT(*) AS order_lines
                FROM OrderItems 
                GROUP BY order_num
                ORDER BY order_lines;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, order_lines=2)
                Result(order_num=20006, order_lines=3)
                Result(order_num=20009, order_lines=3)
                Result(order_num=20007, order_lines=5)
                Result(order_num=20008, order_lines=5)
                """

    def test_exercise2(self):
        """
        2. Write a SQL statement that returns a field named cheapest_item which contains
           the lowest cost item for each vendor (using prod_price in the Products table),
           and sort the results from lowest to highest cost.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT vend_id, MIN(prod_price) AS cheapest_item
                FROM Products 
                GROUP BY vend_id
                ORDER BY cheapest_item;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_id='DLL01', cheapest_item=Decimal('3.49'))
                Result(vend_id='BRS01', cheapest_item=Decimal('5.99'))
                Result(vend_id='FNG01', cheapest_item=Decimal('9.49'))
                """

    def test_exercise3(self):
        """
        3. It’s important to identify the best customers, so write a SQL statement to return
           the order number (order_num in OrderItems table) for all orders of at least 100
           items.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, SUM(quantity) AS items
                FROM OrderItems 
                GROUP BY order_num
                HAVING items >= 100
                ORDER BY items;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, items=Decimal('200'))
                Result(order_num=20007, items=Decimal('400'))
                Result(order_num=20009, items=Decimal('750'))
                """

    def test_exercise4(self):
        """
        4. Another way to determine the best customers is by how much they have spent. Write
           a SQL statement to return the order number (order_num in OrderItems table) for
           all orders with a total price of at least 1000. Hint, for this one you’ll need to
           calculate and sum the total (item_price multiplied by quantity). Sort the results
           by order number.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT order_num, SUM(quantity * item_price) AS money
                FROM OrderItems 
                GROUP BY order_num
                HAVING money >= 1000
                ORDER BY order_num;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(order_num=20005, money=Decimal('1648.00'))
                Result(order_num=20007, money=Decimal('1696.00'))
                Result(order_num=20009, money=Decimal('1867.50'))
                """

    def test_exercise5(self):
        """
        5. What is wrong with the following SQL statement? (Try to figure it out without running it):
        """
        """
        SELECT order_num, COUNT() AS items
        FROM OrderItems
        GROUP BY items
        HAVING COUNT() >= 3
        ORDER BY items, order_num;
        """