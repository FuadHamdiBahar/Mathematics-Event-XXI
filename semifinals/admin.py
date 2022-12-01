from django.contrib import admin

# Register your models here.
from .models import (
    Event,
    SoalSemifinalSD,
    SoalSemifinalSMP,
    SoalSemifinalSMA,
    JawabanSemifinalSD,
    JawabanSemifinalSMP,
    JawabanSemifinalSMA
)

admin.site.register(Event)

admin.site.register(SoalSemifinalSD)
admin.site.register(SoalSemifinalSMP)
admin.site.register(SoalSemifinalSMA)


class AdminJawabanSemifinalSD(admin.ModelAdmin):
    readonly_fields = ['submit_time']


class AdminJawabanSemifinalSMP(admin.ModelAdmin):
    readonly_fields = ['submit_time']


class AdminJawabanSemifinalSMA(admin.ModelAdmin):
    readonly_fields = ['submit_time']


admin.site.register(JawabanSemifinalSD, AdminJawabanSemifinalSD)
admin.site.register(JawabanSemifinalSMP, AdminJawabanSemifinalSMP)
admin.site.register(JawabanSemifinalSMA, AdminJawabanSemifinalSMA)
