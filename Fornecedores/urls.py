from django.urls import path
from Fornecedores.views import fornecedor_view, salvarFornecedor_view, editarFornecedor_view, deleteFornecedor_view

urlpatterns = [
    path('',fornecedor_view, name = "fornecedor_view"),
    path('salvarFornecedor', salvarFornecedor_view, name="salvarFornecedor_view"),
    path('editarFornecedor/<id>',editarFornecedor_view, name="editarFornecedor_view"),
    path('deleteFornecedor/<int:id>', deleteFornecedor_view, name="deleteFornecedor_view")
    
]