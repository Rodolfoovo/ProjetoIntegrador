from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import send_email
from CRUDfuncionario.models import Funcionario
from django.contrib.sessions.models import Session
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
            user = Funcionario.objects.get(username=username)
            criar_sessao(request,user)
            #subject = 'Bem vindo ao Koi.io'
            #message = 'Agradecemos sua preferencia!'
            #send_email(user,subject,message)
            return render(request,'telainicial.html',{"user":user})
        else:
            return render(request,'telainicial.html',{"user":user})
            # return HttpResponse('Usuario ou senha invalidos')
        
def logout_view(request):
    # Verifica se a chave 'userData' existe na sessão antes de acessá-la
    
    if 'user_id' in request.session:
        # Se existir, retorna os dados do usuário
        del request.session['user_id']
        return render(request, 'login.html')
    else:
        return render(request,'login.html')

def criar_sessao(request, user):
    request.session['user_id'] = user.idFuncionario

def verifica_login(request):
    return 'user_id' in request.session

def Perfil_view(request):
    user_id =request.session.get('user_id')
    user = Funcionario.objects.get(idFuncionario=user_id)
    return render(request, 'perfil.html', {"user":user})

def verifica_login(request):
        return 'user_id' in request.session