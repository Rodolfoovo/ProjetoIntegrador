from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from CRUDfuncionario.models import Funcionario
logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST.get("username") 
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user:
            userData = {
                'username': user.username,
                'enderecoFuncionario': user.enderecoFuncionario,
                'cpf':user.cpf,
                'CEP':user.CEP,
                'telefone':user.telefone,
                'funcao':user.funcao,
                'email':user.email
            }
            request.session['userData'] = userData
#            return redirect('logout')
            return redirect('telainicial')
        else:
            return HttpResponse('Email ou senha invalidos')
        
def reset_senha_view(request):
    # Lógica para a página de redefinição de senha
    return render(request, 'Resetarsenha.html')
def logout_view(request):
    userData = request.session['userData']
    return render(request, 'logout.html',{'userData':userData})