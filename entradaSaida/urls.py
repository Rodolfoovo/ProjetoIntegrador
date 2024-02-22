from django.urls import path
from .views import Entrada_Saida
urlpatterns = [
    path('', Entrada_Saida, name='EntradaSaida'),
]