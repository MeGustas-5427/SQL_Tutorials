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


class TestSakilaModel(TestCase):

    def test_get_data(self):
        # Actor表导入数据
        with open("tutorials/create_sakila/data/sakila_actor.json") as file:
            temp = json.loads(file.read())
            Actor.objects.bulk_create([Actor(**i) for i in temp])
            self.assertEqual(Actor.objects.count(), len(temp))

        # Country表导入数据
        with open("tutorials/create_sakila/data/sakila_country.json") as file:
            temp = json.loads(file.read())
            Country.objects.bulk_create([Country(**i) for i in temp])
            self.assertEqual(Country.objects.count(), len(temp))

        # City表导入数据
        with open("tutorials/create_sakila/data/sakila_city.json") as file:
            temp = json.loads(file.read())
            City.objects.bulk_create([City(**i) for i in temp])
            self.assertEqual(City.objects.count(), len(temp))

        # Address表导入数据
        with open("tutorials/create_sakila/data/sakila_address.json") as file:
            temp = json.loads(file.read())
            def pop_location(x:dict) -> dict:
                x.pop("location")
                return x
            Address.objects.bulk_create([Address(**pop_location(i)) for i in temp])
            self.assertEqual(Address.objects.count(), len(temp))

        # Staff表导入数据
        with open("tutorials/create_sakila/data/sakila_staff.json") as file:
            temp = json.loads(file.read())
            def bytes_picture(x:dict) -> dict:
                if x.get("picture"):
                    x["picture"] = bytes(x.get("picture"), encoding="utf-8")
                return x
            Staff.objects.bulk_create([Staff(**bytes_picture(i)) for i in temp])
            self.assertEqual(Staff.objects.count(), len(temp))

        # Store表导入数据
        with open("tutorials/create_sakila/data/sakila_store.json") as file:
            temp = json.loads(file.read())
            Store.objects.bulk_create([Store(**i) for i in temp])
            self.assertEqual(Store.objects.count(), len(temp))

        # Customer表导入数据
        with open("tutorials/create_sakila/data/sakila_customer.json") as file:
            temp = json.loads(file.read())
            def create_date(x:dict) -> dict:
                x["create_date"] = datetime.now(timezone.utc)
                return x
            Customer.objects.bulk_create([Customer(**create_date(i)) for i in temp])
            self.assertEqual(Customer.objects.count(), len(temp))

        # Language表导入数据
        with open("tutorials/create_sakila/data/sakila_language.json") as file:
            temp = json.loads(file.read())
            Language.objects.bulk_create([Language(**i) for i in temp])
            self.assertEqual(Language.objects.count(), len(temp))

        # Film表导入数据
        with open("tutorials/create_sakila/data/sakila_film.json") as file:
            # 修改表字段类型
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE film
                    MODIFY special_features 
                    SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') 
                    DEFAULT NULL
                    COLLATE utf8mb4_general_ci; 
                """)

            temp = json.loads(file.read())
            Film.objects.bulk_create([Film(**i) for i in temp])
            self.assertEqual(Film.objects.count(), len(temp))
            print(Film.objects.all()[0].special_features)

        # Inventory表导入数据
        with open("tutorials/create_sakila/data/sakila_inventory.json") as file:
            temp = json.loads(file.read())
            Inventory.objects.bulk_create([Inventory(**i) for i in temp])
            self.assertEqual(Inventory.objects.count(), len(temp))

        # Rental表导入数据
        with open("tutorials/create_sakila/data/sakila_rental.json") as file:
            temp = json.loads(file.read())
            def set_date(x:dict) -> dict:
                x["rental_date"] = convert_local_timezone(
                    datetime.strptime(x["rental_date"], "%Y-%m-%d %H:%M:%S")
                )
                x["return_date"] = convert_local_timezone(
                    datetime.strptime(x["return_date"], "%Y-%m-%d %H:%M:%S")
                ) if x["return_date"] else x["return_date"]
                return x
            Rental.objects.bulk_create([Rental(**set_date(i)) for i in temp])
            self.assertEqual(Rental.objects.count(), len(temp))

        # Category表导入数据
        with open("tutorials/create_sakila/data/sakila_category.json") as file:
            temp = json.loads(file.read())
            Category.objects.bulk_create([Category(**i) for i in temp])
            self.assertEqual(Category.objects.count(), len(temp))

        # FilmCategory表导入数据
        with open("tutorials/create_sakila/data/sakila_film_category.json") as file:
            temp = json.loads(file.read())
            FilmCategory.objects.bulk_create([FilmCategory(**i) for i in temp])
            self.assertEqual(FilmCategory.objects.count(), len(temp))

        # FilmActor表导入数据
        with open("tutorials/create_sakila/data/sakila_film_actor.json") as file:
            temp = json.loads(file.read())
            FilmActor.objects.bulk_create([FilmActor(**i) for i in temp])
            self.assertEqual(FilmActor.objects.count(), len(temp))

        # FilmText表导入数据
        with open("tutorials/create_sakila/data/sakila_film_text.json") as file:
            temp = json.loads(file.read())
            FilmText.objects.bulk_create([FilmText(**i) for i in temp])
            self.assertEqual(FilmText.objects.count(), len(temp))

        # Payment表导入数据
        with open("tutorials/create_sakila/data/sakila_payment.json") as file:
            temp = json.loads(file.read())
            def set_date(x:dict) -> dict:
                x["payment_date"] = convert_local_timezone(
                    datetime.strptime(x["payment_date"], "%Y-%m-%d %H:%M:%S")
                )
                return x
            Payment.objects.bulk_create([Payment(**set_date(i)) for i in temp])
            self.assertEqual(Payment.objects.count(), len(temp))

    def test_SetCharField(self):
        """
        https://django-mysql.readthedocs.io/en/latest/model_fields/set_fields.html?highlight=SetCharField
        """
        # 修改表字段类型
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE film
                MODIFY special_features 
                SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') 
                DEFAULT NULL
                COLLATE utf8mb4_general_ci; 
            """)
            cursor.execute("SHOW CREATE TABLE film")
            result = [result for result in dictfetchall(cursor)][0]
            print(result)

        # 创建测试数据
        language = Language.objects.create(
            name="test"
        )
        Film.objects.create(
            film_id=1,
            title='ACADEMY DINOSAUR',
            description='A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies',
            release_year=2006,
            language=language,
            rental_duration=6,
            rental_rate='0.99',
            length=86,
            replacement_cost='20.99',
            rating='PG',
            special_features={'Deleted Scenes','Behind the Scenes', 'Trailers'},  # SET
        )

        # 测试使用to_dict()是否能正常序列化
        print(Film.objects.all()[0].to_dict())
        # 测试过滤统计
        print(f'len:', Film.objects.filter(special_features__len=3).count())
        # 测试过滤查询
        print(Film.objects.filter(special_features__contains='Behind the Scenes'))

        print(
            Film.objects.filter(
                Q(special_features__contains='deleted scenes') &
                Q(special_features__contains='trailers')
            )
        )
        # 测试添加/删除元素
        Film.objects.filter(special_features__contains="trailers").update(
            special_features=SetF('special_features').add('Commentaries')
        )
        print(Film.objects.all()[0].special_features)

        Film.objects.update(special_features=SetF('special_features').remove('Behind the Scenes'))
        print('remove(Behind the Scenes):', Film.objects.all()[0].special_features)

        film = Film.objects.all()[0]
        film.special_features = SetF('special_features').remove('Trailers')
        film.save()
        print('remove(Trailers):', Film.objects.all()[0].special_features)

        film.special_features = SetF('special_features').add('Trailers')
        film.save()
        print('add(Trailers):', Film.objects.all()[0].special_features)