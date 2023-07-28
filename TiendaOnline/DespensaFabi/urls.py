from django.urls import path
from DespensaFabi.views import Home, Productos
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', Home, name='Home'),
    path('productos/', Productos, name='productos'),
]
