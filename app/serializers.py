from django_clickhouse.serializers import Django2ClickHouseModelSerializer
from rest_framework import serializers
from .models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields='__all__'


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
