from django.urls import path

from .views import StartFastView, UjianFastView, JawabanResultView

app_name = 'fasts'
urlpatterns = [
    path('result/<exam_code>/', JawabanResultView.as_view(), name='result'),
    path('ujian/<exam_code>/', UjianFastView, name='ujian'),
    path('<exam_code>/', StartFastView.as_view(), name='start'),
]
