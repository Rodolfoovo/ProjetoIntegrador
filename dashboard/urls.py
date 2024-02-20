from django.urls import path
from .views import tela_inicial
from login.views import logout_view
urlpatterns = [
    path('', tela_inicial, name='telainicial'),
    path('logout/',logout_view,name='logout' )
]