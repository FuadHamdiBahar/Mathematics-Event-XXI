from django.contrib import admin

# Register your models here.
from .models import BalloonSoalModel, Event

admin.site.register(Event)

class AdminBalloonSoalModel(admin.ModelAdmin):
    readonly_fields = ['submit_time']
    
admin.site.register(BalloonSoalModel, AdminBalloonSoalModel)