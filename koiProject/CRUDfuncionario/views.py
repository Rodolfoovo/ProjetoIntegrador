from django.shortcuts import render
from .models import Funcionario
# Create your views here.
# Está view está sendo utilizada para poder retornar uma request do sistema, retornando assim um template.
def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "index.html", {"funcionarios": funcionarios})
