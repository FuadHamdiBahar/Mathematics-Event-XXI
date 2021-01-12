from django.urls import path

from .views import CreateInstitutionView

app_name = 'institutions'
urlpatterns = [
    path('create/', CreateInstitutionView.as_view(), name='create'),
]
