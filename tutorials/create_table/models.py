from django.db import models

from utils.models import ModelSerializationMixin
# Create your models here.


class Customers(models.Model, ModelSerializationMixin):

    cust_id = models.CharField(
        "唯一的顾客ID", db_column="cust_id", max_length=10, null=False, primary_key=True
    )
    cust_name = models.CharField("顾客名", max_length=50, null=False)
    cust_address = models.CharField("顾客的地址", max_length=50, null=True)
    cust_city = models.CharField("顾客所在城市", max_length=50, null=True)
    cust_state = models.CharField("顾客所在州", max_length=5, null=True)
    cust_zip = models.CharField("顾客地址邮政编码", max_length=10, null=True)
    cust_country = models.CharField("顾客所在国家", max_length=50, null=True)
    cust_contact = models.CharField("顾客的联系名", max_length=50, null=True)
    cust_email = models.CharField("顾客的e-mail", max_length=255, null=True)

    class Meta:
        verbose_name = "客户表"
        verbose_name_plural = verbose_name
        db_table = "Customers"


class Vendors(models.Model, ModelSerializationMixin):

    vend_id = models.CharField(
        "唯一的供应商ID", max_length=10, db_column="vend_id", null=False, primary_key=True
    )
    vend_name = models.CharField("供应商名", max_length=50, null=False)
    vend_address = models.CharField("供应商的地址", max_length=50, null=True)
    vend_city = models.CharField("供应商所在的城市", max_length=50, null=True)
    vend_state = models.CharField("供应商所在的州", max_length=5, null=True)
    vend_zip = models.CharField("供应商地址邮政编码", max_length=10, null=True)
    vend_country = models.CharField("供应商所在国家", max_length=50, null=True)

    class Meta:
        verbose_name = "供应商表"
        verbose_name_plural = verbose_name
        db_table = "Vendors"


class Orders(models.Model, ModelSerializationMixin):

    order_num = models.IntegerField(
        "唯一的订单号", db_column="order_num", null=False, primary_key=True
    )
    order_date = models.DateTimeField("订单的日期", null=False)
    cust_id = models.ForeignKey(
        Customers,
        to_field="cust_id",
        on_delete=models.CASCADE,
        null=False,
        db_column="cust_id",
        verbose_name="订单顾客的ID",
        help_text="关联到Customer表的cust_id",
    )
    # products = models.ManyToManyField("Products", through='OrderItems')

    class Meta:
        verbose_name = "订单表"
        verbose_name_plural = verbose_name
        db_table = "Orders"


class Products(models.Model, ModelSerializationMixin):

    prod_id = models.CharField(
        "唯一的产品ID", max_length=10, db_column="prod_id", null=False, primary_key=True
    )
    vend_id = models.ForeignKey(
        Vendors,
        to_field="vend_id",
        db_column="vend_id",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="产品供应商ID",
        help_text="关联到Vendors表的vend_id",
    )
    prod_name = models.CharField("产品名", max_length=255, null=False)
    prod_price = models.DecimalField("产品价格", max_digits=8, decimal_places=2, null=False)
    prod_desc = models.TextField("产品描述", null=True)
    # order = models.ManyToManyField(Orders, through='OrderItems')

    class Meta:
        verbose_name = "产品目录表"
        verbose_name_plural = verbose_name
        db_table = "Products"


class OrderItems(models.Model, ModelSerializationMixin):

    order_num = models.ForeignKey(
        Orders,
        to_field="order_num",
        on_delete=models.CASCADE,
        null=False,
        db_column="order_num",
        verbose_name="订单号",
        help_text="关联到Order表的order_num",
    )
    prod_id = models.ForeignKey(
        Products,
        to_field="prod_id",
        on_delete=models.CASCADE,
        null=False,
        db_column="prod_id",
        verbose_name="产品ID",
        help_text="关联到Products表的prod_id",
    )
    order_item = models.IntegerField(
        "订单物品号", null=False, help_text="订单内的顺序"
    )
    quantity = models.IntegerField("物品数量", null=False)
    item_price = models.DecimalField("物品价格", max_digits=8, decimal_places=2, null=False)

    class Meta:
        verbose_name = "订单项目表"
        verbose_name_plural = verbose_name
        db_table = "OrderItems"
        # 多个字段作为一个联合唯一索引
        unique_together = ("order_num", "order_item")
