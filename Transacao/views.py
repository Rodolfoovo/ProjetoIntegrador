from django.shortcuts import render, redirect
from .models import Transacao
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from login.views import login_view, verifica_login
def transacao_view(request):
    if(verifica_login(request)):
        transacoes = Transacao.objects.all()
        return render(request, "transacao.html", {"transacoes": transacoes})
    else:
        return redirect(login_view)

def salvarTransacao_view(request):
    if request.method == 'POST':
        if(verifica_login(request)):
            vDataTransacao = request.POST.get("dataTransacao")
            vTipoTransacao = request.POST.get("tipoTransacao")
            transacao = Transacao(dataTransacao=vDataTransacao, tipoTransacao=vTipoTransacao)
            try:
                transacao.full_clean()
            except ValidationError as e:
                return HttpResponse(f"Erro de validação do formulário: {e}")
            transacao.save()
        return redirect(transacao_view)
    else:
        return redirect(login_view)

def editarTransacao_view(request, id):
    if(verifica_login(request)):
        transacao = Transacao.objects.get(idTransacao=id)
        return render(request, "updateTransacao.html", {"transacao": transacao})
    else:
        return redirect(login_view)

def updateTransacao_view(request, id):
    if(verifica_login(request)):
        if request.method == 'POST':
            transacao = Transacao.objects.get(id=id)
            transacao.dataTransacao = request.POST.get("dataTransacao")
            transacao.tipoTransacao = request.POST.get("tipoTransacao")
            try:
                transacao.full_clean()
            except ValidationError as e:
                return HttpResponse(f"Erro de validação do formulário: {e}")
            transacao.save()
            return redirect(transacao_view)
        else:
            return redirect(login_view)

def deletarTransacao_view(request, id):
    if(verifica_login(request)):
        try:
            transacao = Transacao.objects.get(id=id)
            transacao.delete()
            return redirect(transacao_view)
        except Transacao.DoesNotExist:
            return HttpResponse("Ocorreu um erro ao deletar o objeto.")
    else:
        return redirect(login_view)
