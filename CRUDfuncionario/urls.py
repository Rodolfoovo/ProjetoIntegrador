from django.contrib import admin
from django.urls import path
from .views import home, salvarFuncionario_view, editar_view, update_view, delete_view
#Especifica que ao se entrar na URL irá ser executado o metodo home.
urlpatterns = [
    path('', home),
    path('salvarFuncionario/', salvarFuncionario_view, name = "salvarFuncionario"),
    path('editar/<int:id>', editar_view, name="editar"),
    path('update/<int:id>', update_view, name="update"),
    path('delete/<int:id>', delete_view, name="delete"),
]