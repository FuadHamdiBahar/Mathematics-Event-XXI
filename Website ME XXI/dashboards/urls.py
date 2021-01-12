from django.urls import path

from .views import IndexView

app_name = 'dashboards'
urlpatterns = [
    path('<user_id>', IndexView.as_view(), name='index'),
]
