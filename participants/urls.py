from django.urls import path

from .views import CreateParticipantView, LoginParticipantView,  logout_request

app_name = 'accounts'
urlpatterns = [
    path('create/', CreateParticipantView.as_view(), name='create'),
    path('login/', LoginParticipantView.as_view(), name='login'),
    # path('logout/', LogoutParticipantView.as_view(), name='logout'),
    path('logout/', logout_request, name='logout'),
]
