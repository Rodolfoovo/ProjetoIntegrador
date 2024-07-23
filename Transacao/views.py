from django.shortcuts import render, redirect
from .models import Transacao
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from login.views import login_view, verifica_login
from django.contrib import messages

def transacao_view(request):
    if verifica_login(request):
        transacoes = Transacao.objects.all()
        return render(request, "transacao.html", {"transacoes": transacoes})
    else:
        return redirect(login_view)

def salvarTransacao_view(request):
    if request.method == 'POST':
        if verifica_login(request):
            vDataTransacao = request.POST.get("dataTransacao")
            vTipoTransacao = request.POST.get("tipoTransacao")
            transacao = Transacao(dataTransacao=vDataTransacao, tipoTransacao=vTipoTransacao)
            if(transacao.validar_dados(transacao) == False):
                messages.warning(request,"Dados de edição incorretos!")
                return redirect(salvarTransacao_view)
            transacao.save()
        return redirect(transacao_view)
    else:
        return redirect(login_view)

def editarTransacao_view(request, id):
    if verifica_login(request):
        transacao = Transacao.objects.get(idTransacao=id)
        return render(request, "updateTransacao.html", {"transacao": transacao})
    else:
        return redirect(login_view)

def updateTransacao_view(request, id):
    if verifica_login(request):
        if request.method == 'POST':
            transacao = Transacao.objects.get(id=id)
            transacao.dataTransacao = request.POST.get("dataTransacao")
            transacao.tipoTransacao = request.POST.get("tipoTransacao")
            if(transacao.validar_dados(transacao) == False):
                messages.warning(request,"Dados de edição incorretos!")
                return redirect(editarTransacao_view)
            transacao.save()
            return redirect(transacao_view)
        else:
            return redirect(login_view)

def deletarTransacao_view(request, id):
    if verifica_login(request):
        try:
            transacao = Transacao.objects.get(id=id)
            transacao.delete()
            return redirect(transacao_view)
        except Transacao.DoesNotExist:
            messages.warning(request,"Dados de edição incorretos!")
            return redirect(transacao_view)
    else:
        return redirect(login_view)
