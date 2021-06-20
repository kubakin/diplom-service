from django.urls import path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'site', views.SiteViewSet, basename='site')
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'tariff', views.TariffViewSet, basename='tariff')
router.register(r'profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path("history/", views.HistoryListView.as_view()),
    path("report/", views.ReportListView.as_view()),
    # path("site/<int:pk>/test/", views.TestViewSet.as_view()),
    *router.urls
]
# urlpatterns.append(router.urls[0])