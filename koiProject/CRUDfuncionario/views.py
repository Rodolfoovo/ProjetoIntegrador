from django.shortcuts import render
from CRUDfuncionario.models import Funcionario
from django.shortcuts import redirect
from django.http.response import HttpResponse
# Create your views here.
# Está view está sendo utilizada para poder retornar uma request do sistema, retornando assim um template.
def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "index.html", {"funcionarios": funcionarios})

def salvarFuncionario(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        vnomeFuncionario = request.POST.get("nomeFuncionario")
#        user = User.objects.filter(nomeFuncionario=vnomeFuncionario)
        vNivelDeAcesso = request.POST.get("nivelDeAcesso")
        vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
        vCPF = request.POST.get("CPF")
        vCEP = request.POST.get("CEP")
        vTelefone = request.POST.get("telefone")
#        vSenha = request.POST.get("senha")
        vpassword = request.POST.get("password")
        vFuncao = request.POST.get("funcao")
        Funcionario.objects.create(nivelDeAcesso=vNivelDeAcesso,nomeFuncionario=vnomeFuncionario,
                                enderecoFuncionario=vEnderecoFuncionario,CPF=vCPF,CEP=vCEP,telefone=vTelefone,
                                password=vpassword,funcao=vFuncao)
        funcionarios = Funcionario.objects.all()
        return render(request,"index.html",{"funcionarios":funcionarios})
def editar(request,id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    return render(request, "update.html", {"funcionario": funcionario})

def update(request,id):
    vNome = request.POST.get("nome")
    funcionarios = Funcionario.objects.get(idFuncionario=id)
    funcionarios.nomeFuncionario = vNome
    funcionarios.save()
    return redirect(home)

def delete(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(home)