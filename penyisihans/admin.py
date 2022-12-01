from django.contrib import admin

# Register your models here.
from .models import (
    Event,
    SoalPenyisihanSD,
    SoalPenyisihanSMP,
    SoalPenyisihanSMA,
    JawabanPenyisihanSD,
    JawabanPenyisihanSMP,
    JawabanPenyisihanSMA
)
admin.site.register(Event)

# soal
admin.site.register(SoalPenyisihanSD)
admin.site.register(SoalPenyisihanSMP)
admin.site.register(SoalPenyisihanSMA)

# jawaban


class AdminJawabanPenyisihanSD(admin.ModelAdmin):
    readonly_fields = ['submit_time']


class AdminJawabanPenyisihanSMP(admin.ModelAdmin):
    readonly_fields = ['submit_time']


class AdminJawabanPenyisihanSMA(admin.ModelAdmin):
    readonly_fields = ['submit_time']


admin.site.register(JawabanPenyisihanSD, AdminJawabanPenyisihanSD)
admin.site.register(JawabanPenyisihanSMP, AdminJawabanPenyisihanSMP)
admin.site.register(JawabanPenyisihanSMA, AdminJawabanPenyisihanSMA)
