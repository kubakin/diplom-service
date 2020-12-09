from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

#from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path("history/", views.HistoryListView.as_view()),
    path("data/", views.TestDataView.as_view()),
    path('history/<int:pk>',views.HistoryDetailView.as_view()),
    # path('created/',views.HistoryCreateView.as_view())

]