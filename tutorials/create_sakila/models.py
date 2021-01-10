from django.db import models
from django_mysql.models import SetCharField

from utils import ChoiceEnum
from utils.models import ModelSerializationMixin
# Create your models here.


class Actor(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE actor (
      actor_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      first_name VARCHAR(45) NOT NULL,
      last_name VARCHAR(45) NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (actor_id),
      KEY idx_actor_last_name (last_name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    # 单独使用KEY, 跟使用INDEX没区别
    """

    actor_id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "演员表"
        verbose_name_plural = verbose_name
        db_table = "actor"

        # https://docs.djangoproject.com/en/3.1/ref/models/options/#django.db.models.Options.indexes
        # https://blog.csdn.net/qq_37049050/article/details/80749381
        indexes = [models.Index(fields=['last_name'], name='idx_actor_last_name')]


class Country(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE country (
      country_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      country VARCHAR(50) NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (country_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    country_id = models.SmallAutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "国家表"
        verbose_name_plural = verbose_name
        db_table = "country"


class City(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE city (
      city_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      city VARCHAR(50) NOT NULL,
      country_id SMALLINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (city_id),
      KEY idx_fk_country_id (country_id),
      CONSTRAINT `fk_city_country` FOREIGN KEY (country_id) REFERENCES country (country_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    city_id = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "城市表"
        verbose_name_plural = verbose_name
        db_table = "city"


class Address(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE address (
      address_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      address VARCHAR(50) NOT NULL,
      address2 VARCHAR(50) DEFAULT NULL,
      district VARCHAR(20) NOT NULL,
      city_id SMALLINT UNSIGNED NOT NULL,
      postal_code VARCHAR(10) DEFAULT NULL,
      phone VARCHAR(20) NOT NULL,
      -- Add GEOMETRY column for MySQL 5.7.5 and higher
      -- Also include SRID attribute for MySQL 8.0.3 and higher
      /*!50705 location GEOMETRY */ /*!80003 SRID 0 */ /*!50705 NOT NULL,*/
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (address_id),
      KEY idx_fk_city_id (city_id),
      /*!50705 SPATIAL KEY `idx_location` (location),*/
      CONSTRAINT `fk_address_city` FOREIGN KEY (city_id) REFERENCES city (city_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    address_id = models.SmallAutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "地址表"
        verbose_name_plural = verbose_name
        db_table = "address"


class Staff(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE staff (
      staff_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      first_name VARCHAR(45) NOT NULL,
      last_name VARCHAR(45) NOT NULL,
      address_id SMALLINT UNSIGNED NOT NULL,
      picture BLOB DEFAULT NULL,
      email VARCHAR(50) DEFAULT NULL,
      store_id TINYINT UNSIGNED NOT NULL,
      active BOOLEAN NOT NULL DEFAULT TRUE,
      username VARCHAR(16) NOT NULL,
      password VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (staff_id),
      KEY idx_fk_store_id (store_id),
      KEY idx_fk_address_id (address_id),
      CONSTRAINT fk_staff_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_staff_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    staff_id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, null=True, default=None)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, null=True, default=None)
    picture = models.BinaryField("图片文件", null=True, default=None)
    active = models.BooleanField(default=True)
    store = models.ForeignKey("Store", on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "员工表"
        verbose_name_plural = verbose_name
        db_table = "staff"


class Store(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE store (
      store_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      manager_staff_id TINYINT UNSIGNED NOT NULL,
      address_id SMALLINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (store_id),
      UNIQUE KEY idx_unique_manager (manager_staff_id),
      KEY idx_fk_address_id (address_id),
      CONSTRAINT fk_store_staff FOREIGN KEY (manager_staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_store_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    store_id = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=50)
    manager_staff = models.OneToOneField(
        Staff,
        on_delete=models.RESTRICT,
        related_name="manager",
        verbose_name="店长"
    )
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "电影店表"
        verbose_name_plural = verbose_name
        db_table = "store"


class Customer(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE customer (
      customer_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      store_id TINYINT UNSIGNED NOT NULL,
      first_name VARCHAR(45) NOT NULL,
      last_name VARCHAR(45) NOT NULL,
      email VARCHAR(50) DEFAULT NULL,
      address_id SMALLINT UNSIGNED NOT NULL,
      active BOOLEAN NOT NULL DEFAULT TRUE,
      create_date DATETIME NOT NULL,
      last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (customer_id),
      KEY idx_fk_store_id (store_id),
      KEY idx_fk_address_id (address_id),
      KEY idx_last_name (last_name),
      CONSTRAINT fk_customer_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_customer_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    customer_id = models.SmallAutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT, verbose_name="电影店")
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, verbose_name="客户住址")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, null=True, default=None)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField("创建时间")
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "客户表"
        verbose_name_plural = verbose_name
        db_table = "customer"
        indexes = [models.Index(fields=['last_name'], name='idx_last_name')]


class Language(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE language (
      language_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      name CHAR(20) NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (language_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    language_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "语言种类"
        verbose_name_plural = verbose_name
        db_table = "language"


class Film(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE film (
      film_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      title VARCHAR(128) NOT NULL,
      description TEXT DEFAULT NULL,
      release_year YEAR DEFAULT NULL,
      language_id TINYINT UNSIGNED NOT NULL,
      original_language_id TINYINT UNSIGNED DEFAULT NULL,
      rental_duration TINYINT UNSIGNED NOT NULL DEFAULT 3,
      rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
      length SMALLINT UNSIGNED DEFAULT NULL,
      replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
      rating ENUM('G','PG','PG-13','R','NC-17') DEFAULT 'G',
      special_features SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') DEFAULT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (film_id),
      KEY idx_title (title),
      KEY idx_fk_language_id (language_id),
      KEY idx_fk_original_language_id (original_language_id),
      CONSTRAINT fk_film_language FOREIGN KEY (language_id) REFERENCES language (language_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_film_language_original FOREIGN KEY (original_language_id) REFERENCES language (language_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    film_id = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, default=None)

    YEAR_CHOICES = lambda : [(r, r) for r in range(1901, 2156)]
    release_year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES() , null=True, default=None)
    language = models.ForeignKey(Language, on_delete=models.RESTRICT)
    original_language = models.ForeignKey(Language, on_delete=models.RESTRICT, related_name="original_film")
    rental_duration = models.PositiveSmallIntegerField(default=3)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2, default='4.99')
    length = models.PositiveSmallIntegerField(null=True, default=None)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2, default='19.99')
    class Rating(ChoiceEnum):
        G = 'G'
        R = 'R'
        PG = 'PG'
        PG_13 = 'PG-13'
        NC_17 = 'NC-17'
    rating = models.CharField(max_length=5, choices=Rating, default=Rating.G)

    class Special(ChoiceEnum):
        Trailers = 'Trailers'
        Commentaries = 'Commentaries'
        Deleted_Scenes = 'Deleted Scenes'
        Behind_the_Scenes = 'Behind the Scenes'
    special_features = SetCharField(
        base_field=models.CharField(max_length=20),
        size=4,
        max_length=83,  # 20*4+3个逗号
        choices=Special,
        null=True,
        default=None,
        verbose_name="特殊功能"
    )
    actors = models.ManyToManyField(Actor, through='FilmActor', verbose_name='电影演员')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "电影表"
        verbose_name_plural = verbose_name
        db_table = "film"

        indexes = [models.Index(fields=['title'], name='idx_title')]


class Inventory(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE inventory (
      inventory_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
      film_id SMALLINT UNSIGNED NOT NULL,
      store_id TINYINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (inventory_id),
      KEY idx_fk_film_id (film_id),
      KEY idx_store_id_film_id (store_id,film_id),
      CONSTRAINT fk_inventory_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_inventory_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    inventory = models.AutoField(primary_key=True)
    film = models.ForeignKey(Store, on_delete=models.RESTRICT)
    store = models.ForeignKey(Film, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "库存表"
        verbose_name_plural = verbose_name
        db_table = "inventory"
        indexes = [models.Index(fields=['store', 'film'], name='idx_store_id_film_id')]  # 联合索引


class Rental(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE rental (
      rental_id INT NOT NULL AUTO_INCREMENT,
      rental_date DATETIME NOT NULL,
      inventory_id MEDIUMINT UNSIGNED NOT NULL,
      customer_id SMALLINT UNSIGNED NOT NULL,
      return_date DATETIME DEFAULT NULL,
      staff_id TINYINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (rental_id),
      UNIQUE KEY  (rental_date,inventory_id,customer_id),
      KEY idx_fk_inventory_id (inventory_id),
      KEY idx_fk_customer_id (customer_id),
      KEY idx_fk_staff_id (staff_id),
      CONSTRAINT fk_rental_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_rental_inventory FOREIGN KEY (inventory_id) REFERENCES inventory (inventory_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_rental_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    rental_id = models.SmallAutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.RESTRICT, verbose_name="库存")
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="客户")
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT, verbose_name="员工")
    rental_date = models.DateTimeField("出租时间")
    return_date = models.DateTimeField("返还时间", null=True, default=None)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "出租表"
        verbose_name_plural = verbose_name
        db_table = "rental"

        # 联合唯一
        constraints = [
            models.UniqueConstraint(
                fields=["rental_date", "inventory", "customer"],
                name="film_rental"
            )
        ]


class Category(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE category (
      category_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      name VARCHAR(25) NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (category_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    category_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=25)
    films = models.ManyToManyField(Film, through='FilmCategory', verbose_name='电影栏目')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "栏目"
        verbose_name_plural = verbose_name
        db_table = "category"


class FilmCategory(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE film_category (
      film_id SMALLINT UNSIGNED NOT NULL,
      category_id TINYINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (film_id, category_id),
      CONSTRAINT fk_film_category_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_film_category_category FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    film = models.ForeignKey(Film, on_delete=models.RESTRICT, verbose_name="电影")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name="栏目")
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "电影栏目"
        verbose_name_plural = verbose_name
        db_table = "film_category"
        # 联合唯一键(django不支持设置联合主键), unique_together用法即将被淘汰
        constraints = [
            models.UniqueConstraint(
                fields=["category", "film"],
                name="idx_category_film"
            )
        ]

class FilmActor(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE film_actor (
      actor_id SMALLINT UNSIGNED NOT NULL,
      film_id SMALLINT UNSIGNED NOT NULL,
      last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (actor_id,film_id),
      KEY idx_fk_film_id (`film_id`),
      CONSTRAINT fk_film_actor_actor FOREIGN KEY (actor_id) REFERENCES actor (actor_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_film_actor_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    actor = models.ForeignKey(Actor, on_delete=models.RESTRICT, verbose_name="演员")
    film = models.ForeignKey(Film, on_delete=models.RESTRICT, verbose_name="电影")
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "电影演员表"
        verbose_name_plural = verbose_name
        db_table = "film_actor"
        # 联合唯一键(django不支持设置联合主键), unique_together用法即将被淘汰
        constraints = [
            models.UniqueConstraint(
                fields=["actor", "film"],
                name="idx_actor_film"
            )
        ]


class FilmText(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE film_text (
      film_id SMALLINT NOT NULL,
      title VARCHAR(255) NOT NULL,
      description TEXT,
      PRIMARY KEY  (film_id),
      FULLTEXT KEY idx_title_description (title,description)  # 创建联合全文索引列
    ) DEFAULT CHARSET=utf8mb4;
    # django3.1版本仅支持PostgreSQL的全文搜索
    # MySQL的全文搜索需要亲自到数据库设置并在python业务代码上用SQL语句实现全文搜索
    # https://zhuanlan.zhihu.com/p/35675553
    """
    film_id = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "电影详情表"
        verbose_name_plural = verbose_name
        db_table = "film_text"


class Payment(models.Model, ModelSerializationMixin):
    """
    CREATE TABLE payment (
      payment_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
      customer_id SMALLINT UNSIGNED NOT NULL,
      staff_id TINYINT UNSIGNED NOT NULL,
      rental_id INT DEFAULT NULL,
      amount DECIMAL(5,2) NOT NULL,
      payment_date DATETIME NOT NULL,
      last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY  (payment_id),
      KEY idx_fk_staff_id (staff_id),
      KEY idx_fk_customer_id (customer_id),
      CONSTRAINT fk_payment_rental FOREIGN KEY (rental_id) REFERENCES rental (rental_id) ON DELETE SET NULL ON UPDATE CASCADE,
      CONSTRAINT fk_payment_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
      CONSTRAINT fk_payment_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    # Django会自动为所有 models.ForeignKey 列创建索引
    """
    payment_id = models.SmallAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="客户")
    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT, verbose_name="员工")
    rental = models.ForeignKey(Rental, on_delete=models.RESTRICT, verbose_name="出租")
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField("支付时间")
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "付款表"
        verbose_name_plural = verbose_name
        db_table = "payment"
