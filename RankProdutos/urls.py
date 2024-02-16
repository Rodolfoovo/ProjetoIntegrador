from django.urls import path
from .views import Rank_Produtos
urlpatterns = [
    path('', Rank_Produtos, name='RankProdutos'),
]