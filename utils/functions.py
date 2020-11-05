import datetime

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
