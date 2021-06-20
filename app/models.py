from django.contrib.auth.models import User
from django_clickhouse.models import ClickHouseSyncModel
from django.db import models


class History(ClickHouseSyncModel):
    date = models.DateField("Дата действия")
    action = models.TextField("Действие", default='some action')
    device = models.TextField('Устройство', default='no info', null=True, blank=True)
    ip = models.TextField('IP address',default='no info', null=True, blank=True)
    location = models.TextField('Location of user', default='no info', null=True, blank=True)
    siteOfUser = models.TextField('Сайт, откуда пришел пользователь', default='site.com', null=False, blank=False)
    userName = models.TextField('Имя пользователя на сайте', default='user', null=False, blank=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_of_user')
    balance = models.FloatField(default=0)


class Site(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_of_site')

    def __str__(self):
        return self.name


#Модель для отчетов
class SiteReport(models.Model):
    data = models.DateTimeField('Дата отчета', auto_now=True)
    cnt = models.IntegerField('Count')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='reply_in_site')
    class Meta:
        db_table = 'app_sitereport'


class Tariff(models.Model):
    name = models.CharField('Название тарифа', max_length=100)
    miniText = models.CharField('Краткое описание', max_length=500)
    text = models.TextField('Описание')
    instruction = models.TextField('Инструкция')
    priceGetData = models.FloatField('Цена за сохранение')
    pricePostData = models.FloatField('Цена за анализ')
    def __str__(self):
        return self.name
    # toSite = models.ManyToManyField(Site, related_name='tariff_for_site')


class SiteInTariff(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='tariff_for_site')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)


class Dogovor(models.Model):
    date = models.DateTimeField(auto_created=True, auto_now=True)
    type = models.CharField('Тип договора', max_length=100)
    text = models.TextField('Текст договора')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dogovor_for_user')

    def __str__(self):
        return self.type