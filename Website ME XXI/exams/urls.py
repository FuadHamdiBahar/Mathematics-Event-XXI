from django.urls import path

from .views import (
    BabakPenyisihan3,
    SemiFinal,
    BalloonGameView,
    BalloonGameDetailView,
    BalloonGameSoalView,
    FastGameView,
    FinishView,
)

app_name = 'exams'
urlpatterns = [
    path('penyisihan/<tingkat>/<exam_code>',
         BabakPenyisihan3, name='penyisihan'),
    path('semifinal/<tingkat>/<exam_code>', SemiFinal, name='semifinal'),
    path('balloon/<exam_code>', BalloonGameView.as_view(), name='balloon'),
    path('balloon/<exam_code>/<pk>',
         BalloonGameDetailView.as_view(), name='detail_balloon'),
    path('balloon/soal/<exam_code>/<id_soal>',
         BalloonGameSoalView.as_view(), name='soal_balloon'),
    path('fast/<exam_code>/<id_soal>', FastGameView.as_view(), name='fast'),
    path('finish/<id>', FinishView.as_view(), name='finish'),
]
