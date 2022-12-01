from django.urls import path

from .views import (
    BalloonSoalView,
    BalloonSoalDetailView,
    BalloonJawabView,
    StartBalloonView
)

app_name = 'balloons'
urlpatterns = [
    path('rules/<exam_code>/', StartBalloonView.as_view(), name='start'),
    path('jawab/<exam_code>/<pk>/', BalloonJawabView.as_view(), name='jawab'),
    path('<exam_code>/<pk>/', BalloonSoalDetailView.as_view(), name='detail'),
    path('<exam_code>/', BalloonSoalView.as_view(), name='show'),
]
