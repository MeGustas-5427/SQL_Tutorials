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

    """
    MySQL基础教程
        4.6.1 查看表的列结构:
            DESC 表名;
        5.3.1 字符串类型的种类
            CHAR	    0-255           bytes   定长字符串
            VARCHAR	    0-65535         bytes	变长字符串
            TEXT	    0-65_535        bytes	长文本数据
            LONGTEXT	0-4_294_967_295 bytes	极大文本数据
            (定长字符串:不足长度会用空格填充,读取的时候根据各个RDMBS决定是否自动删除空格)
            (一般 utf-8 编码下，一个汉字 字符 占用 3 个 bytes)
            (一般 gbk   编码下，一个汉字 字符 占用 2 个 bytes)
        5.4.1 日期与时间类型的种类
            数据类型                       范围                               格式              用途
            DATE	             1000-01-01~9999-12-31	                 YYYY-MM-DD	        日期值
            TIME	  	       '-838:59:59'~'838:59:59'	                  HH:MM:SS	    时间值或持续时间
            YEAR    	               1901~2155	                        YYYY	        年份值
            DATETIME  (1000-01-01 00:00:00)~(9999-12-31 23:59:59)	YYYY-MM-DD HH:MM:SS	混合日期和时间值
    """

    # 17.1 表创建基础
    def test_create_table(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (       #  AUTO_INCREMENT: 自增(自动连续编号功能)
                    id INT AUTO_INCREMENT PRIMARY KEY,  # 主键默认NOT NULL并且UNIQUE(不许重复)
                    prod_id CHAR(10) NOT NULL,  # 输入多于指定字符数的数据不会报错而是忽略多出来的数据,             
                    vend_id CHAR(10) NOT NULL,  # 除非在SQL Models设置为STRICT_TRANS_TABLES
                    prod_name CHAR(254) NOT NULL,  # 4.1之后版本:CHAR(数字:字符数)和VARCHAR(数字:字符数)
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000) NULL,
                    create_time TIME,
                    create_date DATE,
                    create_year YEAR DEFAULT '2020',  # DEFAULT:设置默认值
                    date_time DATETIME UNIQUE
                )
                CHARSET=utf8mb4;  # 可以选择性增加指定字符编码, 但一般创建数据库设置了字符编码为utf8mb4的话就不用再设置了.
            """)
            """
            提示：替换现有的表
                在创建新的表时，指定的表名必须不存在，否则会出错。防止意外覆盖已有的表，
                SQL要求首先手工删除该表（请参阅后面的内容），然后再重建它，而不是简单地
                用创建表语句覆盖它。
            """
            print(cursor.fetchone())

    # 17.1.2 使用NULL值
    def test_null(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    prod_id CHAR(10) NOT NULL,
                    vend_id CHAR(10) NOT NULL,
                    prod_name CHAR(254) NOT NULL,
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000)   # NULL为默认设置, 可以不填NULL
                );
            """)
            """
            注意：理解NULL
                不要把NULL值与空字符串相混淆. NULL值是没有值，不是空字符串。 
                如果指定''(两个单引号，其间没有字符)，这在NOT NULL列中是允 
                许的。空字符串是一个有效的值，它不是无值。NULL值用关键字NULL 
                而不是空字符串指定。
            """
            print(cursor.fetchone())

    # 17.1.3 指定默认值
    def test_default_value(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (
                    prod_id CHAR(10) NOT NULL,
                    vend_id CHAR(10) NOT NULL,
                    prod_name CHAR(254) NOT NULL,
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000) NOT NULL DEFAULT 'balabala' # 默认值为'balabala'
                );
            """)
            print(cursor.fetchone())

    # 17.2 更新表
    def test_alter_table(self):
        """
        更新表定义,可以使用ALTER TABLE语句.虽然所有的DBMS都支持ALTER TABLE,
        但它们所允许更新的内容差别很大.以下是使用ALTER TABLE时需要考虑的事情。
            - 理想情况下，不要在表中包含数据时对其进行更新。应该在表的设计
              过程中充分考虑未来可能的需求，避免今后对表的结构做大改动。
            - 所有的DBMS都允许给现有的表增加列，不过对所增加列的数据类型
              (以及NULL和DEFAULT的使用）有所限制。
            - 许多DBMS不允许删除或更改表中的列。
            - 多数DBMS允许重新命名表中的列。
            - 许多DBMS限制对已经填有数据的列进行更改，对未填有数据的列几
              乎没有限制。

        复杂的表结构更改一般需要手动删除过程，它涉及以下步骤：
            (1) 用新的列布局创建一个新表；
            (2) 使用INSERT SELECT语句从旧表复制数据到新表。
                有必要的话，可以使用转换函数和计算字段；
            (3) 检验包含所需数据的新表；
            (4) 重命名旧表（如果确定，可以删除它）；
            (5) 用旧表原来的名字重命名新表；
            (6) 根据需要，重新创建触发器、存储过程、索引和外键。
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (
                    prod_id CHAR(10) NOT NULL,
                    vend_id CHAR(10) NOT NULL,
                    prod_name CHAR(254) NOT NULL,
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000) NOT NULL DEFAULT 'balabala' # 默认值为'balabala'
                );
            """)

            # 增加列(ADD)
            cursor.execute("""
                ALTER TABLE TestTable
                ADD phone CHAR(20) FIRST,  # FIRST 为指定列的位置为第一列
                ADD sex INT AFTER phone;   # AFTER phone: 指定sex列在phone列的后面  
            """)

            # 修改列(MODIFY) mysql基础教程 6.2
            # 修改列, 包含的数据类型必须具有兼容性,并符合新的设定.
            # 譬如原字符串100, 新设置字符串长度上限少于100会出问题.
            # 原则上列中存在数据,则不应该再修改列的数据类型.
            cursor.execute("""
                ALTER TABLE TestTable
                MODIFY prod_name CHAR(1000) NOT NULL,  # 修改列数据类型
                MODIFY vend_id CHAR(10) NOT NULL FIRST;  # 修改列的顺序(必须含数据类型和相关设置, 即使不变也要填)
            """)

            # 初始化AUTO_INCREMENT
            cursor.execute("""
                ALTER TABLE TestTable
                AUTO_INCREMENT=1;  # 若表数据清除后, 可初始化AUTO_INCREMENT, 恢复从1开始自增记录
            """)
            # 删除列(DROP)
            cursor.execute("""
                ALTER TABLE TestTable
                DROP COLUMN phone;
            """)
            print(cursor.fetchone())

    # 17.3 删除表
    def test_drop_table(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable (prod_id CHAR(10) NOT NULL);
            """)

            # 删除TestTable表
            cursor.execute("""
                DROP TABLE IF EXISTS TestTable;  # IF EXISTS:如果存在则删除TestTable
            """)
            """
            提示: 使用关系规则防止意外删除
                许多DBMS允许强制实施有关规则，防止删除与其他表相关联的表。在 
                实施这些规则时，如果对某个表发布一条DROP TABLE语句，且该表是 
                某个关系的组成部分，则DBMS将阻止这条语句执行，直到该关系被删 
                除为止。如果允许，应该启用这些选项，它能防止意外删除有用的表。
            """

    # 17.4 重命名表
    def test_rename_table(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE TestTable
                (
                    prod_id CHAR(10) NOT NULL,
                    vend_id CHAR(10) NOT NULL,
                    prod_name CHAR(254) NOT NULL,
                    prod_price DECIMAL(8,2) NOT NULL,
                    prod_desc VARCHAR(1000) NOT NULL DEFAULT 'balabala' # 默认值为'balabala'
                );
            """)
        # 列改名(CHANGE)
        cursor.execute("""
            ALTER TABLE TestTable
            CHANGE sex gender TINYINT;  # 修改列名时候必须含数据类型, 即使数据类型不打算改变.
        """)

    # 6.12.2 创建索引(MySQL基础教程)
    def test_create_index(self):
        """
            实际上，创建了索引并不代表一定会缩短查找时间。因为根据查找条件的不同，有时候不需要用到索引，而
        且在某些情况下，使用索引反而会花费更多的时间。
            例如，人们都说在相同值较多（重复值较多）的情况下最好不要创建索引。我们举一个极端的例子，当某列
        中只有“YES"和"NO”这两个值时，即使在该列上创建索引也不会提高处理速度。
            另外，当对创建了索引的表进行更新时，也需要对已经存在的索引信息进行维护。所以，在使用索引的情况
        下，检索速度可能会变快，但与此同时，更新速度也很可能会变慢。
            在使用索引的情况下，即使索引在创建过程中出现了错误，查找结果也不会受到任何影响。创建索引只会影
        响数据库整体的处理速度。
            索引的创建是影响整个数据库处理效率的重要问题。我们把这种提高处理效率的对策称为调优(tuning)。
        如何调优就要看数据库工程师的技能了。
        """
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
            # 创建索引格式:CREATE INDEX 自定义索引名 ON 表名 (列名);
            cursor.execute("""
                CREATE INDEX index_prod_id ON TestTable (prod_id);
            """)
            # 确定索引设置是否成功:SHOW INDEX FROM TestTable \G  # '\G'替代';', 会纵向显示列值, 清晰一些.

    # 6.12.4 删除索引(MySQL基础教程)
    def test_drop_index(self):
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
            # 删除索引格式:CREATE INDEX 索引名 ON 表名;
            cursor.execute("""
                DROP INDEX index_prod_id ON TestTable;
            """)

    # 课后练习
    def test_exercise1(self):
        """
        1. Using INSERT and columns specified, add yourself to the Customers table.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE Vendors
                ADD vend_web CHAR(255); 
            """)

    def test_z_exercise2(self):
        """
        2. Make a backup copy of your Orders and OrderItems tables.
        """
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE Vendors
                ADD vend_web CHAR(255); 
            """)

            cursor.execute("""
                UPDATE Vendors
                SET vend_web = 'https://megustas.com'
                WHERE vend_web IS NULL;
            """)
            cursor.execute("""
                SELECT vend_web FROM Vendors;
            """)
            for result in namedtuplefetchall(cursor):  # 读取所有
                print(result)
                """
                Result(vend_web='https://megustas.com')
                Result(vend_web='https://megustas.com')
                Result(vend_web='https://megustas.com')
                Result(vend_web='https://megustas.com')
                Result(vend_web='https://megustas.com')
                Result(vend_web='https://megustas.com')
                """
