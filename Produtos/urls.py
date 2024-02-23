from django.urls import path
from Produtos.views import produtos_view, editarProdutos_view, deleteProduto_view
urlpatterns = [
    path('', produtos_view),
    path('produtos/',produtos_view, name="produtos_view"),
    path('editarProdutos/<id>',editarProdutos_view, name="editarProdutos_view"),
    path('deleteProduto/<int:id>', deleteProduto_view, name="deleteProduto_view")
]