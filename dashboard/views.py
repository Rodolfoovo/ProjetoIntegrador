from django.shortcuts import render, redirect
from login.views import login_view, verifica_login
def tela_inicial(request):
    if(verifica_login(request)):
        return render(request, 'telainicial.html')
    else:
        return redirect(login_view)
