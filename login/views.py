from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import send_email
from CRUDfuncionario.models import Funcionario
import logging
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
                'CPF':user.CPF,
                'CEP':user.CEP,
                'telefone':user.telefone,
                'funcao':user.funcao,
                'email':user.email
            }
            user = Funcionario.objects.get(username=username)
            request.session['userData'] = userData
            #subject = 'Bem vindo ao Koi.io'
            #message = 'Agradecemos sua preferencia!'
            #send_email(user,subject,message)
            return render(request,'telainicial.html',{"user":user})
        else:
            return HttpResponse('Usuario ou senha invalidos')
        
def logout_view(request):
    # Verifica se a chave 'userData' existe na sessão antes de acessá-la
    userData = request.session.get('userData')
    if userData:
        # Se existir, retorna os dados do usuário
        request.session.clear()
        return render(request, 'login.html')
    else:
        # Se não existir, retorna uma resposta vazia ou outra resposta adequada
        return HttpResponse('Usuário não está logado ou dados não encontrados na sessão')