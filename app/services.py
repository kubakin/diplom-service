import random

from django_ipgeobase.models import IPGeoBase
from .constructor import Constructor
from app.serializers import MySerializer
from .models import Dogovor


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


def filterQuery(model, dct):
    fields = ['concat', 'count']
    sqlQuery = Constructor
    sqlQuery.stps(sqlQuery, step='day')
    sqlQuery.fromRangeOrTable(sqlQuery, dct['site'])
    qs = model.get_database().select(Constructor.get_qs_concat(Constructor))
    return qs, fields

def create_dogovor(usr, tp, data1, data2):
    text = ''
    if(tp == 'О Пополнение баланса'):
        text = '<p>Данный договор подверждает, что {} пополнил баланс на {}</p>'.format(usr.first_name, data1)
        text += '<p>Текущий баланс составляет {}</p>'.format(data2)
    elif (tp=='О предоставлении услуг'):
        text = '<p>Данный договор подверждает, что {} заключил договор о {}'.format(usr.first_name, tp)
        text+='<p>Была предоставлена услуга {} для сайта {}'.format(data2.name, data1.name)
    elif (tp=='Заключение договора'):
        pass
    b = Dogovor(type=tp, user=usr, text=text)
    b.save()