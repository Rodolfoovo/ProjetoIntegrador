from django.contrib import admin
from django.urls import path
from .views import Funcionarios, salvarFuncionario_view, editar_view, update_view, delete_view
#Especifica que ao se entrar na URL irá ser executado o metodo home.
urlpatterns = [
    path('', Funcionarios),
    path('salvarFuncionario/', salvarFuncionario_view, name = "salvarFuncionario_view"),
    path('editar/<int:id>', editar_view, name="editar_view"),
    path('update/<int:id>', update_view, name="update_view"),
    path('delete/<int:id>', delete_view, name="delete_view"),
]