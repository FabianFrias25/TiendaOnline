from django.urls import path
from DespensaFabi.views import Home
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', Home, name='Home'),
]
