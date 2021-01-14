#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'
import json
from datetime import datetime, timezone

import pytz
from django.conf import settings
from django.test import TestCase
from django.db import connection
from django.db.models import Q
from django_mysql.models import SetF

from tutorials.create_sakila.models import *


# Create your tests here.
from utils.functions import dictfetchall


def convert_local_timezone(time_in: datetime) -> datetime:
    """
    用来将输入的datetime格式的本地时间转化为utc时区时间
    :param time_in: datetime.datetime格式的本地时间
    :return:输出仍旧是datetime.datetime格式，但已经转换为utc时间
    """
    local = pytz.timezone(settings.TIME_ZONE)
    local_dt = local.localize(time_in, is_dst=None)
    time_utc = local_dt.astimezone(pytz.utc)
    return time_utc


def read_file(part: str) -> list:
    with open(part) as file:
        return json.loads(file.read())


def delete_data():
    Payment.objects.all().delete()
    FilmText.objects.all().delete()
    FilmActor.objects.all().delete()
    FilmCategory.objects.all().delete()
    Category.objects.all().delete()
    Rental.objects.all().delete()
    Inventory.objects.all().delete()
    Film.objects.all().delete()
    Language.objects.all().delete()
    Customer.objects.all().delete()
    Staff.objects.all().delete()
    Store.objects.all().delete()
    Address.objects.all().delete()
    City.objects.all().delete()
    Country.objects.all().delete()
    Actor.objects.all().delete()


def insert_data() -> tuple:
    # Actor表导入数据
    actor = read_file("tutorials/create_sakila/data/sakila_actor.json")
    Actor.objects.bulk_create([Actor(**i) for i in actor])

    # Country表导入数据
    country = read_file("tutorials/create_sakila/data/sakila_country.json")
    Country.objects.bulk_create([Country(**i) for i in country])

    # City表导入数据
    city = read_file("tutorials/create_sakila/data/sakila_city.json")
    City.objects.bulk_create([City(**i) for i in city])

    # Address表导入数据
    address = read_file("tutorials/create_sakila/data/sakila_address.json")

    def pop_location(x: dict) -> dict:
        x.pop("location")
        return x

    Address.objects.bulk_create([Address(**pop_location(i)) for i in address])

    # Staff表导入数据
    staff = read_file("tutorials/create_sakila/data/sakila_staff.json")

    def bytes_picture(x: dict) -> dict:
        if x.get("picture"):
            x["picture"] = bytes(x.get("picture"), encoding="utf-8")
        return x

    Staff.objects.bulk_create([Staff(**bytes_picture(i)) for i in staff])

    # Store表导入数据
    store = read_file("tutorials/create_sakila/data/sakila_store.json")
    Store.objects.bulk_create([Store(**i) for i in store])

    # Customer表导入数据
    customer = read_file("tutorials/create_sakila/data/sakila_customer.json")

    def create_date(x: dict) -> dict:
        x["create_date"] = datetime.now(timezone.utc)
        return x

    Customer.objects.bulk_create([Customer(**create_date(i)) for i in customer])

    # Language表导入数据
    language = read_file("tutorials/create_sakila/data/sakila_language.json")
    Language.objects.bulk_create([Language(**i) for i in language])

    # Film表导入数据
    film = read_file("tutorials/create_sakila/data/sakila_film.json")
    # 修改表字段类型
    with connection.cursor() as cursor:
        cursor.execute(
            """
            ALTER TABLE film
            MODIFY special_features 
            SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') 
            DEFAULT NULL
            COLLATE utf8mb4_general_ci; 
        """
        )
    Film.objects.bulk_create([Film(**i) for i in film])

    # Inventory表导入数据
    inventory = read_file("tutorials/create_sakila/data/sakila_inventory.json")
    Inventory.objects.bulk_create([Inventory(**i) for i in inventory])

    # Rental表导入数据
    rental = read_file("tutorials/create_sakila/data/sakila_rental.json")

    def set_date(x: dict) -> dict:
        x["rental_date"] = convert_local_timezone(
            datetime.strptime(x["rental_date"], "%Y-%m-%d %H:%M:%S")
        )
        x["return_date"] = (
            convert_local_timezone(
                datetime.strptime(x["return_date"], "%Y-%m-%d %H:%M:%S")
            )
            if x["return_date"]
            else x["return_date"]
        )
        return x

    Rental.objects.bulk_create([Rental(**set_date(i)) for i in rental])

    # Category表导入数据
    category = read_file("tutorials/create_sakila/data/sakila_category.json")
    Category.objects.bulk_create([Category(**i) for i in category])

    # FilmCategory表导入数据
    film_category = read_file("tutorials/create_sakila/data/sakila_film_category.json")
    FilmCategory.objects.bulk_create([FilmCategory(**i) for i in film_category])

    # FilmActor表导入数据
    film_actor = read_file("tutorials/create_sakila/data/sakila_film_actor.json")
    FilmActor.objects.bulk_create([FilmActor(**i) for i in film_actor])

    # FilmText表导入数据
    film_text = read_file("tutorials/create_sakila/data/sakila_film_text.json")
    FilmText.objects.bulk_create([FilmText(**i) for i in film_text])

    # Payment表导入数据
    payment = read_file("tutorials/create_sakila/data/sakila_payment.json")

    def set_date(x: dict) -> dict:
        x["payment_date"] = convert_local_timezone(
            datetime.strptime(x["payment_date"], "%Y-%m-%d %H:%M:%S")
        )
        return x

    Payment.objects.bulk_create([Payment(**set_date(i)) for i in payment])

    return (
        actor,
        country,
        city,
        address,
        staff,
        store,
        customer,
        language,
        film,
        inventory,
        rental,
        category,
        film_category,
        film_actor,
        film_text,
        payment,
    )


class TestSakilaModel(TestCase):
    def test_get_data(self):
        actor, country, city, address, staff, store, customer, language, film, inventory, rental, category, film_category, film_actor, film_text, payment = insert_data()

        self.assertEqual(Actor.objects.count(), len(actor))
        self.assertEqual(Country.objects.count(), len(country))
        self.assertEqual(City.objects.count(), len(city))
        self.assertEqual(Address.objects.count(), len(address))
        self.assertEqual(Staff.objects.count(), len(staff))
        self.assertEqual(Store.objects.count(), len(store))
        self.assertEqual(Customer.objects.count(), len(customer))
        self.assertEqual(Language.objects.count(), len(language))
        self.assertEqual(Film.objects.count(), len(film))
        print(Film.objects.all()[0].special_features)
        self.assertEqual(Inventory.objects.count(), len(inventory))
        self.assertEqual(Rental.objects.count(), len(rental))
        self.assertEqual(Category.objects.count(), len(category))
        self.assertEqual(FilmCategory.objects.count(), len(film_category))
        self.assertEqual(FilmActor.objects.count(), len(film_actor))
        self.assertEqual(FilmText.objects.count(), len(film_text))
        self.assertEqual(Payment.objects.count(), len(payment))

    def test_SetCharField(self):
        """
        https://django-mysql.readthedocs.io/en/latest/model_fields/set_fields.html?highlight=SetCharField
        """
        # 修改表字段类型
        with connection.cursor() as cursor:
            cursor.execute(
                """
                ALTER TABLE film
                MODIFY special_features 
                SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') 
                DEFAULT NULL
                COLLATE utf8mb4_general_ci; 
            """
            )
            cursor.execute("SHOW CREATE TABLE film")
            result = [result for result in dictfetchall(cursor)][0]
            print(result)

        # 创建测试数据
        language = Language.objects.create(name="test")
        Film.objects.create(
            film_id=1,
            title="ACADEMY DINOSAUR",
            description="A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies",
            release_year=2006,
            language=language,
            rental_duration=6,
            rental_rate="0.99",
            length=86,
            replacement_cost="20.99",
            rating="PG",
            special_features={"Deleted Scenes", "Behind the Scenes", "Trailers"},  # SET
        )

        # 测试使用to_dict()是否能正常序列化
        print(Film.objects.all()[0].to_dict())
        # 测试过滤统计
        print(f"len:", Film.objects.filter(special_features__len=3).count())
        # 测试过滤查询
        print(Film.objects.filter(special_features__contains="Behind the Scenes"))

        print(
            Film.objects.filter(
                Q(special_features__contains="deleted scenes")
                & Q(special_features__contains="trailers")
            )
        )
        # 测试添加/删除元素
        Film.objects.filter(special_features__contains="trailers").update(
            special_features=SetF("special_features").add("Commentaries")
        )
        print(Film.objects.all()[0].special_features)

        Film.objects.update(
            special_features=SetF("special_features").remove("Behind the Scenes")
        )
        print("remove(Behind the Scenes):", Film.objects.all()[0].special_features)

        film = Film.objects.all()[0]
        film.special_features = SetF("special_features").remove("Trailers")
        film.save()
        print("remove(Trailers):", Film.objects.all()[0].special_features)

        film.special_features = SetF("special_features").add("Trailers")
        film.save()
        print("add(Trailers):", Film.objects.all()[0].special_features)
