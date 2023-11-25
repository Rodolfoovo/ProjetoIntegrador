from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home
#Especifica que ao se entrar na URL irá ser executado o metodo home.
urlpatterns = [
    path('', home),
]