from abc import ABCMeta, abstractmethod
import random

from django.shortcuts import get_object_or_404

from app.models import Tariff
from app.serializers import MySerializer


class BaseClass():
    __metaclass__ = ABCMeta
    @abstractmethod
    def useMethodML(self, model, name, site):
        """Использовать метод ML"""
        pass


class FakeAlgo(BaseClass):
    def __init__(self, model):
        self.model = model
    def useMethodML(self, model, name,site):
        MySerializer.serialize(MySerializer, model.objects.filter(userName=name, siteOfUser=site))
        return random.uniform(0, 1)

def useAlgo(algo, model, name, site):
    algs = dict()
    price = 0
    for i in algo:
        queryset = Tariff.objects.all()
        tariff = get_object_or_404(queryset, pk=i)
        print(tariff)
        if tariff.name == 'AntiFraud algorithm':
            algs[tariff.name] = FakeAlgo.useMethodML(FakeAlgo, model, name, site)
            print(tariff)
            price+=tariff.pricePostData
        if tariff.name == 'one more tariff':
            algs[tariff.name] = FakeAlgo.useMethodML(FakeAlgo, model, name, site)
            price+=tariff.pricePostData
    # print(algs)
    return algs, price
