from django.urls import path

from .views import HomeDataView

app_name = 'data'
urlpatterns = [
    path('', HomeDataView.as_view(), name='home'),
]
