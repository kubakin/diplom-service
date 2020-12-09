"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), # admin panel
    path('auth/', include('djoser.urls')), # Библиотека для авторизации
    path('auth/', include('djoser.urls.jwt')), # Библиотека для авторизации
    path('api/', include('rest_framework.urls')), # url api
    path('apiv2/', include('app.urls')), # url api
    path('auth/', include('djoser.urls.authtoken')), # Библиотека для авторизации

]
