import datetime
import random

import pytz
from celery import shared_task
# from demoapp.models import Widget
from app.clickhouse_models import ClickHouseHistory
from app.models import Site
from app.serializers import SiteSerializer
from service.celery import app
import random


@app.task
def printer():
    data = datetime.datetime.now(tz=pytz.UTC)
    rnd = random.randint(0,1)
    if(rnd == 1) :
        instance = ClickHouseHistory.objects.create(action='qq', date=data
                                                  , ip='185.90.100.111', device='device', location='location',
                                                  siteOfUser='qqqq', userName='qqqq')

    print('WORK WORK WORK')
    return False


@app.task
def getStat():
    dt = datetime.datetime.now(tz=pytz.UTC)
    dt = dt.astimezone(pytz.timezone('Europe/Moscow'))
    start_date = datetime.datetime.fromtimestamp(dt.timestamp()-60)
    start_date = start_date.astimezone(pytz.timezone('Europe/Moscow'))
    print(start_date)
    counterSite = Site.objects.all()
    serializer = SiteSerializer(counterSite, many=True)
    data = serializer.data
    for i in data:
        cnt = ClickHouseHistory.objects.filter(ClickHouseHistory.date>start_date, siteOfUser=i['name'], ).count()
        usr = Site.objects.filter(name=i['name']).first()
