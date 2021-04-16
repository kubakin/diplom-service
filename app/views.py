import datetime
import random
from django.http import QueryDict
from rest_framework.response import Response
from .clickhouse_models import ClickHouseHistory
from rest_framework.views import APIView
from .serializers import MySerializer, ReportSerializer
from ipware import get_client_ip

from .services import getGeo, parseData, detectFraud, filterQuery


class ReportListView(APIView):
    def get(self, request):
        qd = QueryDict(request.META['QUERY_STRING'])
        # print("SELECT toMonth(date) AS month, toYear(date) AS year,count() AS count FROM `clickhousehistory` where siteOfUser='{}' GROUP BY toMonth(date), toYear(date)".format(qd['site']))
        # qs = ClickHouseHistory.objects.filter().aggregate(month='toMonth(date)', count='count()').group_by('month')
        # qs = ClickHouseHistory.get_database().select("SELECT toMonth(date) AS month, toYear(date) AS year,count() AS count　"
        #                                               "FROM `clickhousehistory` where siteOfUser='{}'"
        #                                               "GROUP BY toMonth(date), toYear(date)".format(qd['site']))
        # tst = list(tst)
        # for i in  tst:
        #     print(i.count)
        srlz = ReportSerializer
        qs, srlz.fields = filterQuery(ClickHouseHistory, qd)
        # srlz.fields.append('month')
        # srlz.fields.append('year')
        jsn = srlz.serialize(ReportSerializer, qs)
        return Response(jsn)


class HistoryListView(APIView):

    def get(self, request):
        cl, rt = get_client_ip(request) # Получение IP пользователя
        # print(cl) #ip
        queryset = ClickHouseHistory.objects.all()
        jsn = MySerializer.serialize(MySerializer, queryset)
        return Response(jsn)

    def post(self, request):
        flag = random.randint(0,1)
        device = request.META['HTTP_USER_AGENT']
        location = getGeo()
        data = parseData(request)
        fraud = detectFraud(ClickHouseHistory, 'one more user', "http://127.0.0.1:8080")
        instance = ClickHouseHistory.objects.create(action=data('action'), date=datetime.datetime.today()
                    ,ip='185.90.100.111', device=device, location=location, siteOfUser=data('siteOfUser'), userName=data('userName'))
        if flag == 1:
            return Response(fraud)

        return Response('Ok')

