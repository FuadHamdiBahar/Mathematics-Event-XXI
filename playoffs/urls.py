from django.urls import path

from .views import (
    StartPlayoffView,
    UjianPlayoffView,
)

app_name = 'playoffs'
urlpatterns = [
    path('start_playoff/<exam_code>/',
         StartPlayoffView.as_view(), name='start_playoff'),
    path('ujian_playoff/<exam_code>/',
         UjianPlayoffView.as_view(), name='ujian_playoff'),
]
