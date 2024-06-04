from django.shortcuts import render
from .models import Transacao
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your views here.

def transacao_view(request):
    transacoes = Transacao.objects.all()
    return render(request,"transacao.html",{transacoes: "transacoes"})

def salvarTransacao_view(request):
    if request.method == 'POST':
        vDataTransacao = request.POST("dataTransacao")
        vTipoTransacao = request.POST("tipoTransacao")
        transacao = Transacao(
            dataTransacao=vDataTransacao, 
            tipoTransacao=vTipoTransacao
        )
        try:
            transacao.full_clean()
        except ValidationError as e:
            return HttpResponse(f"Erro de validacao do formulário: {e}")
        transacao = Transacao.objects.create(
            dataTransacao = vDataTransacao,
            tipoTransacao=vTipoTransacao
        )
    return redirect(transacao_view)

def editarTransacao_view(request,id):
    transacao = Transacao.objects.get(idTransacao=id)
    return render(request, "updateTransacao.html",{"transacao":transacao})

