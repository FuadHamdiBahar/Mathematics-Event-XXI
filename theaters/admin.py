from django.contrib import admin

# Register your models here.
from .models import JawabanTheaterModelSMP, JawabanTheaterModelSMA, Event

admin.site.register(Event)
admin.site.register(JawabanTheaterModelSMP)
admin.site.register(JawabanTheaterModelSMA)
