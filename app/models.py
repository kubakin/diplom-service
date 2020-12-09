from django.contrib.auth.models import User
from django.db import models
import datetime
class History(models.Model):
    date = models.DateField("Дата действия")
    action = models.TextField("Действие")
    def __str__(self):
        return self.action

class Visitor(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    historyOfUser = models.ForeignKey(History, verbose_name ="История пользователя", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TestData(models.Model):
    a = models.CharField('a', max_length=50, blank=False, null=False)
    b = models.CharField('b', max_length=50, blank=False, null=False)
    c = models.CharField('c', max_length=50, blank=False, null=False)