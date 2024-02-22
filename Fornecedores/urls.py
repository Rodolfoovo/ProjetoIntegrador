from django.urls import path
from Fornecedores.views import fornecedor_view, salvarFornecedor_view

urlpatterns = [
    path('',fornecedor_view, name = "fornecedor_view"),
    path('salvarFornecedor', salvarFornecedor_view, name="salvarFornecedor_view")
]