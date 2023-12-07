from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home, salvarFuncionario, editar, update, delete
#Especifica que ao se entrar na URL irá ser executado o metodo home.
urlpatterns = [
    path('', home),
    path('salvarFuncionario/', salvarFuncionario, name = "salvarFuncionario"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]