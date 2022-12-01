from django.urls import path

from .views import StartTheaterView, UjianTheatreView

app_name = 'theaters'
urlpatterns = [
    path('ujian/<exam_code>/<id>', UjianTheatreView, name='ujian'),
    path('<exam_code>', StartTheaterView.as_view(), name='start'),
]