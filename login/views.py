from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
import logging
from CRUDfuncionario.models import Funcionario
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        idFuncionario = request.POST.get("idFuncionario") 
        password = request.POST.get("password")

        user = authenticate(request,username=idFuncionario,password=password)
        if user:
            return HttpResponse('Login efetuado com Sucesso!')
        else:
            return HttpResponse('Email ou senha invalidos')
        
def reset_senha_view(request):
    # Lógica para a página de redefinição de senha
    return render(request, 'Resetarsenha.html')
