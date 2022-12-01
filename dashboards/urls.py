from django import urls
from django.urls import path

from .views import (
    AboutView,
    DocumentView,
    Home,
    IndexView,
    TutorialRegistrasiView,
    DataViewSD,
    DataViewSMP,
    DataViewSMA,
    Jadwal,
    GambaranUmum,
)

app_name = 'dashboards'
urlpatterns = [
    path('jadwal/', Jadwal.as_view(), name='jadwal'),
    path('gambaran/', GambaranUmum.as_view(), name='gambaran_umum'),
    path('dashboards/<user_id>', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('document/', DocumentView.as_view(), name='document'),
    path('datasd/', DataViewSD.as_view(), name='datasd'),
    path('datasmp/', DataViewSMP.as_view(), name='datasmp'),
    path('datasma/', DataViewSMA.as_view(), name='datasma'),
    path('tutorial/', TutorialRegistrasiView.as_view(), name='tutorial'),
    path('', Home.as_view(), name='home'),
]
