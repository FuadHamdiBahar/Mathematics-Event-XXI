from django.urls import path

from .views import StartPenyisihanView, UjianPenyisihanView, PenyisihanResultView

app_name = 'penyisihans'
urlpatterns = [
    path('result/<exam_code>/', PenyisihanResultView.as_view(), name='result'),
    path('ujian/<exam_code>/', UjianPenyisihanView, name='ujian'),
    path('<exam_code>/', StartPenyisihanView.as_view(), name='start'),
]
