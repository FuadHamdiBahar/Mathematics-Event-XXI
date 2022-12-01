"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('participants.urls', namespace='accounts')),
    path('balloons/', include('balloons.urls', namespace='balloons')),
    path('', include('dashboards.urls', namespace='dashboards')),
    path('fasts/', include('fasts.urls', namespace='fasts')),
    path('institutions/', include('institutions.urls', namespace='institutions')),
    path('penyisihan/', include('penyisihans.urls', namespace='penyisihans')),
    path('playoffs/', include('playoffs.urls', namespace='playoffs')),
    path('semifinal/', include('semifinals.urls', namespace='semifinals')),
    path('theaters/', include('theaters.urls', namespace='theaters')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
