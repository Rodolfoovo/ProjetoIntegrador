from django.urls import path
from .views import transacao_view, salvarTransacao_view, editarTransacao_view, deletarTransacao_view

urlpatterns = [
    path('', transacao_view, name="transacao_view"),
    path('salvarTransacao/', salvarTransacao_view, name="salvarTransacao_view"),
    path('editarTransacao/<int:id>', editarTransacao_view, name="editarTransacao_view"),
    path('deletarTransacao/<int:id>', deletarTransacao_view, name="deletarTransacao_view")
]
