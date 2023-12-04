from django.shortcuts import render
from .models import Funcionario
# Create your views here.
# Está view está sendo utilizada para poder retornar uma request do sistema, retornando assim um template.
def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "index.html", {"funcionarios": funcionarios})

def salvarFuncionario(request):
    vnomeFuncionario = request.POST.get("nomeFuncionario")
    vNivelDeAcesso = request.POST.get("nivelDeAcesso")
    vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
    vCPF = request.POST.get("CPF")
    vCEP = request.POST.get("CEP")
    vTelefone = request.POST.get("telefone")
    vSenha = request.POST.get("senha")
    vFuncao = request.POST.get("funcao")
    Funcionario.objects.create(nivelDeAcesso=vNivelDeAcesso,nomeFuncionario=vnomeFuncionario,
                               vEnderecoFuncionario=vEnderecoFuncionario,CPF=vCPF,CEP=vCEP,telefone=vTelefone,
                               senha=vSenha,funcao=vFuncao)
    funcionarios = Funcionario.objects.all()
    return render(request,"index.html",{"funcionarios":funcionarios})
