from django.contrib import admin

# Register your models here.
from .models import(
    SoalPlayoff,
    PlayOffPenyisihan,
    PlayOffSemifinal,
    PlayOffBalloon,
    PlayOffFast,
    PlayOffTheatre,
)

admin.site.register(SoalPlayoff)
admin.site.register(PlayOffPenyisihan)
admin.site.register(PlayOffSemifinal)
admin.site.register(PlayOffBalloon)
admin.site.register(PlayOffFast)
admin.site.register(PlayOffTheatre)
