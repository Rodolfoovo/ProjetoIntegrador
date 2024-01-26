from django.urls import path
from .views import tela_inicial
urlpatterns = [
    path('', tela_inicial, name='telainicial'),
]