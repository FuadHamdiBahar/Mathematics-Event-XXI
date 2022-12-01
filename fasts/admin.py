from django.contrib import admin

# Register your models here.
from .models import SoalFastModel, JawabanFastModel, Event
admin.site.register(Event)
admin.site.register(SoalFastModel)


# jawaban
class AdminJawabanFastModel(admin.ModelAdmin):
    readonly_fields = ['submit_time']


admin.site.register(JawabanFastModel, AdminJawabanFastModel)
