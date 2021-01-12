from django.contrib import admin

# Register your models here.
from .models import (
    Soal,
    BalloonSoal,
    FastSoal,
    Jawaban,
    JawabanSemiFinal,
    JawabanBalloon,
    JawabanFast,
)
admin.site.register(Soal)
admin.site.register(BalloonSoal)
admin.site.register(FastSoal)
admin.site.register(Jawaban)
admin.site.register(JawabanSemiFinal)
admin.site.register(JawabanBalloon)
admin.site.register(JawabanFast)
