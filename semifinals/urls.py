from django.urls import path

from .views import StartSemiFinalsView, UjianSemifinalView, SemifinalResultView

app_name = 'semifinals'
urlpatterns = [
    path('result/<exam_code>/', SemifinalResultView.as_view(), name='result'),
    path('ujian/<exam_code>/', UjianSemifinalView, name='ujian'),
    path('<exam_code>/', StartSemiFinalsView.as_view(), name='start'),
]
