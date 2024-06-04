from django.shortcuts import render
from .models import Transacao
# Create your views here.

def transacao_view(request):
    transacoes = Transacao.objects.all()
    return render(request,"transacao.html",{transacoes: "transacoes"})

#def salvarTransacao_view(request):
