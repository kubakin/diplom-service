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


class Site(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return self.name