from unicodedata import name
from django.urls import path
from .views import autenticar, index, perfil, registro, desconectar

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('login/', autenticar, name='login'),
    path('logout/', desconectar, name='logout'),
]
