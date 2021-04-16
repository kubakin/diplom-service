import random

from django_ipgeobase.models import IPGeoBase

from app.serializers import MySerializer


def getGeo(ip='185.90.100.111'):
    ipgeobases = IPGeoBase.objects.by_ip('212.49.98.48')  # пока заглушка, т.к. локальный не идентифицируется
    if ipgeobases.exists():
        ipgeobase = ipgeobases[0]
        # print(ipgeobase.country)  # 'RU' - Страна
        # print(ipgeobase.district)  # Округ (для указанного ip - Уральский федеральный округ)
        # print(ipgeobase.region)  # Регион (Свердловская область)
        # print(ipgeobase.city)  # Населенный пункт (Екатеринбург)
        # print(ipgeobase.ip_block)  # IP-блок, в который попали (212.49.96.0 - 212.49.127.255)
        # print(ipgeobase.start_ip, ipgeobase.end_ip)  # (3560005632, 3560013823), IP-блок в числовом формате
        # print(ipgeobase.latitude, ipgeobase.longitude)  # (56.837814, 60.596844), широта и долгота
        return '{} {}'.format(ipgeobase.country, ipgeobase.city)
    return 'None'


def parseData(request):
    if 'data' in request.data:
        def haveKey(key):
            if key in request.data['data']:
                return request.data['data'][key]
            return 'No {}'.format(key)
        return haveKey
    return 'No data'
    # print(request.data['data']['action'])


def detectFraud(model, name, site):
    MySerializer.serialize(MySerializer, model.objects.filter(userName=name, siteOfUser=site))
    return random.uniform(0,1)


# def some():
#     for i in range(12):

def filterQuery(model, dct):
    day = ''
    asDay = ''
    fields = ['year', 'month', 'count']
    if 'range' in dct:
        if dct['range'] == 'lastYear':
            pass
    if 'step' in dct:
        if dct['step'] == 'day':
            day = 'toDayOfYear(date)'
            asDay = 'AS day,'
            fields.append('day')
            print(day)
        if dct['step'] == 'hour':
            day = 'toHour(date)'
            asDay = 'AS hour,'
            fields.append('hour')
            print(day)
    # print("SELECT {0} {2} toMonth(date) AS month, toYear(date) AS year,count() AS count　"
    #                                              "FROM `clickhousehistory` where siteOfUser='{1}'"
    #                                              "GROUP BY {0}, toMonth(date), toYear(date)".format(day, dct['site'], asDay))
    qs = model.get_database().select("SELECT {0} {2} toMonth(date) AS month, toYear(date) AS year,count() AS count　"
                                                 "FROM `clickhousehistory` where siteOfUser='{1}'"
                                                 "GROUP BY {0}, toMonth(date), toYear(date) order by hour".format(day, dct['site'], asDay))
    # print(qs)
    return qs, fields