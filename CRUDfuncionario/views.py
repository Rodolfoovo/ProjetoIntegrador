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
        try:
            usuarioAux= Funcionario.objects.get(username=request.POST["username"])
            if usuarioAux:
                return render(request,"index.html", {'msg':'Erro! Já existe este nome no sistema'})
        except Funcionario.DoesNotExist:
            vusername = request.POST.get("username")
    #        user = User.objects.filter(nomeFuncionario=vnomeFuncionario)
            vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
            vCPF = request.POST.get("CPF")
            vCEP = request.POST.get("CEP")
            vTelefone = request.POST.get("telefone")
            vpassword = request.POST.get("password")
            vFuncao = request.POST.get("funcao")
            Funcionario.objects.create(nivelDeAcesso=1,username=vusername,
                                    enderecoFuncionario=vEnderecoFuncionario,CPF=vCPF,CEP=vCEP,telefone=vTelefone,
                                    password=vpassword,funcao=vFuncao)
            funcionarios = Funcionario.objects.all()
            return render(request,"index.html",{"funcionarios":funcionarios})
def editar(request,id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    return render(request, "update.html", {"funcionario": funcionario})

def update(request,id):
    vusername = request.POST.get("username")
    funcionarios = Funcionario.objects.get(idFuncionario=id)
    funcionarios.username = vusername
    funcionarios.save()
    return redirect(home)

def delete(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(home)