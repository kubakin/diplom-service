from django.forms import model_to_dict
from django_clickhouse.serializers import Django2ClickHouseModelSerializer
from djoser.conf import User
import datetime as dt
from djoser.serializers import UserSerializer as mdl
from rest_framework import serializers
from .models import Site, SiteReport, Tariff, SiteInTariff, Profile, Dogovor


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteReport
        fields = '__all__'


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'name', 'miniText', 'url')


class SiteInTariffSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name')
    tariff_name = serializers.CharField(source='tariff.name')
    class Meta:
        model = SiteInTariff
        fields = '__all__'


class TariffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):
    # tracks = serializers.serializers.StringRelatedField(many=True)
    tariff_for_site = SiteInTariffSerializer(many=True, read_only=True)
    class Meta:
        model = Site
        # fields=('id', 'name','url')
        fields='__all__'

    # def to_representation(self, instance):
    #     return model_to_dict(instance)


class SiteDetailReportSerializer(serializers.ModelSerializer):
    reply_in_site = ReplySerializer(many=True)
    class Meta:
        model = Site
        fields=('name', 'reply_in_site')


class MySerializer:
    fields = ['action', 'date', 'device', 'userName', 'siteOfUser', 'date', 'location', 'ip']
    dct = dict()
    lst = []

    def serialize(self, qs):
        self.lst = []
        for i in qs:
            for j in self.fields:
                self.dct[j] = (getattr(i, j, None))
            self.lst.append(self.dct)
            self.dct = {}
        return self.lst


class ReportSerializer(MySerializer):
    fields = ['count']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class DogovorSerializer(serializers.ModelSerializer):
    # date_str = serializers.
    class Meta:
        model = Dogovor
        fields = '__all__'

    def to_representation(self, instance):
        # print(instance.date.strftime('%m/%d/%Y'))
        return {'id': instance.pk, 'type': instance.type, 'text':instance.text, 'date': instance.date.strftime('%m/%d/%Y')}


class UserSerializer(serializers.ModelSerializer):
    owner_of_site = SiteSerializer(many=True, read_only=True)
    profile_of_user = ProfileSerializer()
    dogovor_for_user = DogovorSerializer(many=True, read_only=True)
    class Meta:
        model = User
        # fields = ('id',)
        exclude = ('password',)