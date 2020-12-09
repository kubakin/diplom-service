# from django.shortcuts import render
# from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
# from rest_framework.permissions import IsAuthenticated
# from .models import userProfile
# from .permissions import IsOwnerProfileOrReadOnly
# from .serializers import userProfileSerializer
from rest_framework.response import Response
from .models import History, TestData
from django.core import serializers
from rest_framework.views import APIView
from rest_framework import generics,mixins
from .serializers import HistoryListSerializer, HistoryDetailSerializer, HistoryCreateSerializer, TestDataSerializer
class HistoryListView(generics.ListCreateAPIView):
    serializer_class = HistoryListSerializer
    def get_queryset(self):
        test = History.objects.all()
        return test
    def post(self, request,*args, **kwargs):
        data = self.create(request, *args, **kwargs)
        # Тут мы можем добавлять условия по действияем
        # Например перед покупкой отсылаем наши данных алгоритму detect_frodo
        #print(data.data['id'])
        return data
class HistoryDetailView(generics.RetrieveAPIView):
    serializer_class = HistoryDetailSerializer
    queryset = History.objects.all()

class TestDataView(generics.ListCreateAPIView):
    serializer_class = TestDataSerializer
    def get_queryset(self):
        test = TestData.objects.all()
        return test
    def post(self, request,*args, **kwargs):
        data = self.create(request, *args, **kwargs)
        data.data['response']='Ваши данные получены'
        return data