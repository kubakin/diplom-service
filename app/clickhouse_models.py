from django_clickhouse.clickhouse_models import ClickHouseModel
from django_clickhouse.engines import MergeTree
from django_clickhouse.serializers import Django2ClickHouseModelSerializer
from infi.clickhouse_orm import fields
from app.models import History
import datetime


class ClickHouseHistory(ClickHouseModel):
    django_model = History
    django_model_serializer = Django2ClickHouseModelSerializer
    date = fields.DateTimeField(default=datetime.datetime.now())
    action = fields.StringField(default='')
    device = fields.StringField(default='')
    ip = fields.StringField(default='')
    location = fields.StringField(default='')
    siteOfUser = fields.StringField(default='')
    userName = fields.StringField(default='Неизвестный пользователь')
    engine = MergeTree('date', ('date',))
