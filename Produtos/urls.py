from django.urls import path
from Produtos.views import produtos_view, fornecedor_view
urlpatterns = [
    path('', produtos_view),
    path('produtos/',produtos_view, name="produtos_view"),
    path('fornecedor/',fornecedor_view, name = "fornecedor_view")
]