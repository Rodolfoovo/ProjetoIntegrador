from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from CRUDfuncionario.models import Funcionario
# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        idFuncionario = request.POST.get("idFuncionario") 
        senha = request.POST.get("senha")
        user = Funcionario.objects.filter(idFuncionario=idFuncionario, senha=senha)
        if user:
            return HttpResponse('autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')