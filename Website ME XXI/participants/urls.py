from django.urls import path

from .views import CreateParticipantView, LoginParticipantView, LogoutParticipantView

app_name = 'participants'
urlpatterns = [
    path('create/', CreateParticipantView.as_view(), name='create'),
    path('login/', LoginParticipantView.as_view(), name='login'),
    path('logout/', LogoutParticipantView.as_view(), name='logout'),
]
