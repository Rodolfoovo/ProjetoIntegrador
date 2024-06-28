from django.contrib import admin
from django.urls import path
from .views import Funcionarios, salvarFuncionario_view, editarFuncionario_view, updateFuncionario_view, deleteFuncionario_view
#Especifica que ao se entrar na URL irá ser executado o metodo home.
urlpatterns = [
    path('', Funcionarios, name="funcionario"),
    path('salvarFuncionario/', salvarFuncionario_view, name = "salvarFuncionario_view"),
    path('editar/<int:id>', editarFuncionario_view, name="editarFuncionario_view"),
    path('update/<int:id>', updateFuncionario_view, name="updateFuncionario_view"),
    path('delete/<int:id>', deleteFuncionario_view, name="deleteFuncionario_view"),
]