import datetime
from collections import namedtuple

import pytz
from django.conf import settings



def convert_timezone(time_in: datetime.datetime) -> datetime.datetime:
    """
    用来将系统自动生成的datetime格式的utc时区时间转化为本地时间
    :param time_in: datetime.datetime格式的utc时间
    :return:输出仍旧是datetime.datetime格式，但已经转换为本地时间
    """
    time_utc = time_in.replace(tzinfo=pytz.timezone("UTC"))
    time_local = time_utc.astimezone(pytz.timezone(settings.TIME_ZONE))
    return time_local


def dictfetchall(cursor):
    "从cursor获取所有行数据转换成一个字典"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def namedtuplefetchall(cursor):
    "从cursor获取所有行数据转换成一个namedtuple数据类型"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]