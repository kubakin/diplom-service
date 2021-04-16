from django.urls import path
from . import views


urlpatterns = [
    path("history/", views.HistoryListView.as_view()),
    path("report/", views.ReportListView.as_view()),

    # path('history/<int:pk>',views.HistoryDetailView.as_view()),

]