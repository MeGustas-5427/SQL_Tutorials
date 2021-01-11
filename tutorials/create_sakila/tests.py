#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__MeGustas__'

from django.test import TestCase
from django.db import connection
from django.db.models import Q
from django_mysql.models import SetF

from tutorials.create_sakila.models import *


# Create your tests here.
from utils.functions import dictfetchall


class TestSakilaModel(TestCase):

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