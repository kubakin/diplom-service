import datetime
import random
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from djoser.conf import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .clickhouse_models import ClickHouseHistory
from rest_framework.views import APIView

from .methodsML import useAlgo
from .models import Site, Tariff, SiteInTariff, Profile, Dogovor
from .serializers import MySerializer, ReportSerializer, SiteSerializer, SiteDetailReportSerializer, UserSerializer, \
    TariffSerializer, TariffDetailSerializer, ProfileSerializer
from ipware import get_client_ip

from .services import getGeo, parseData, detectFraud, filterQuery, create_dogovor


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class TariffViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tariff.objects.all()
        serializer_class = TariffSerializer(queryset, context={'request': request},  many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Tariff.objects.all()
        tariff = get_object_or_404(queryset, pk=pk)
        serializer_class = TariffDetailSerializer(tariff)
        return Response(serializer_class.data)


class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()

    @action(methods=['get'], detail=True, url_path='report', url_name='report')
    def show_reports(self, request, pk=None):
        # print(request.__dict__)
        queryset = Site.objects.all()
        site = get_object_or_404(queryset, pk=pk)
        # print(site)
        serializer = SiteDetailReportSerializer(site)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, url_path='gettariff', url_name='gettariff')
    def create_order_to_tariff(self, request, pk=None):
        # print(request.user.first_name)
        # create_dogovor(request.user, 'О предоставлении услуг')
        # print(pk)
        # print(request.data['tariff'])
        queryset = Site.objects.all()
        site = get_object_or_404(queryset, pk=pk)
        queryset = Tariff.objects.all()
        tariff = get_object_or_404(queryset, pk=request.data['tariff'])
        b = SiteInTariff(site=site, tariff=tariff)
        b.save()
        print(site, tariff)
        create_dogovor(request.user, 'О предоставлении услуг', site,tariff)
        # test = Dogovor(user=request.user, text='qwe', )
        return Response({'status':'success'})


class ReportListView(APIView):
    def get(self, request):
        qd = QueryDict(request.META['QUERY_STRING'])
        srlz = ReportSerializer
        qs, srlz.fields = filterQuery(ClickHouseHistory, qd)
        jsn = srlz.serialize(ReportSerializer, qs)
        return Response(jsn)


class HistoryListView(APIView):

    def get(self, request):
        cl, rt = get_client_ip(request)  # Получение IP пользователя
        # print(cl) #ip
        queryset = ClickHouseHistory.objects.all()
        jsn = MySerializer.serialize(MySerializer, queryset)
        return Response(jsn)

    def post(self, request):
        device = request.META['HTTP_USER_AGENT']
        location = getGeo()
        data = parseData(request)
        site = Site.objects.filter(name='http://127.0.0.1:8080')
        value = get_object_or_404(site, name='http://127.0.0.1:8080')
        profile = Profile.objects.all()
        profile = get_object_or_404(profile, user=value.id)
        # profile.balance = 100
        # print(value.owner)
        queryset = SiteInTariff.objects.filter(site=value.id).values_list('tariff', flat=True)

        if data('type') == 'buy':
            rs, price = useAlgo(queryset, ClickHouseHistory, 'one more user', "http://127.0.0.1:8080")
            print(rs)
            profile.balance-=price
            profile.save()
            return Response(rs)
        profile.balance -= 0.01
        profile.save()
        instance = ClickHouseHistory.objects.create(action=data('action'), date=datetime.datetime.today()
                    ,ip='185.90.100.111', device=device, location=location, siteOfUser=data('siteOfUser'), userName=data('userName'))
        return Response('Ok')

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    @action(methods=['post'], detail=True, url_path='topup', url_name='topup')
    def top_up_balance(self, request, pk=None):
        print(request.user)
        add = 100
        queryset = Profile.objects.filter(user=request.user.id)
        qs = get_object_or_404(queryset, user=request.user.id)
        qs.balance +=add
        qs.save()
        create_dogovor(request.user, 'О Пополнение баланса', add, qs.balance)
        return Response({'status':'success'})
