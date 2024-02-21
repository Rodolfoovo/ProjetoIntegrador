from django.urls import path
from .views import tela_inicial
from login.views import logout_view
from CRUDfuncionario.views import home
from Produtos.views import produtos_view
urlpatterns = [
    path('', tela_inicial, name='telainicial'),
    path('logout/',logout_view,name='logout' ),
    path('home/', home , name='home'),
    path('produtos/',produtos_view,name='produtos')
]