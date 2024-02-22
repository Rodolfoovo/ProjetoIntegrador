from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import send_email
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
                'cpf':user.cpf,
                'CEP':user.CEP,
                'telefone':user.telefone,
                'funcao':user.funcao,
                'email':user.email
            }
            request.session['userData'] = userData
            subject = 'Bem vindo ao Koi.io'
            message = 'Agradecemos sua preferencia!'
            send_email(user,subject,message)
            return redirect('telainicial')
        else:
            return HttpResponse('Usuario ou senha invalidos')
        
def logout_view(request):
    userData = request.session['userData']
    return render(request, 'logout.html',{'userData':userData})