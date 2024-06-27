from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from login.views import login_view, verifica_login

def Funcionarios(request):
    if(verifica_login(request)):
        funcionarios = Funcionario.objects.all()
        return render(request, "funcionarios.html", {"funcionarios": funcionarios})
    else:
        return redirect(login_view)

def salvarFuncionario_view(request):
    if request.method == 'GET':
        return render(request, "funcionarios.html")
    elif request.method == 'POST':
        # Verifica se já existe um usuário com o mesmo username
        novo_funcionario = Funcionario(
                nivelDeAcesso=1,
                username=request.POST.get("username"),
                enderecoFuncionario=request.POST.get("enderecoFuncionario"),
                CPF=request.POST.get("CPF"),
                CEP=request.POST.get("CEP"),
                telefone=request.POST.get("telefone"),
                password=request.POST.get("password"),
                funcao=request.POST.get("funcao"),
                email=request.POST.get("email")
            )
        try:
            novo_funcionario.full_clean()
            usuarioAux = Funcionario.objects.get(username=request.POST.get("username"))
            return redirect(Funcionarios)
        except ValidationError as e:
                return HttpResponse(f"Erro de validacao do formulário: {e}")
        except Funcionario.DoesNotExist:
            # Autentica o novo usuário
            novo_funcionario =Funcionario.objects.create_user(
                nivelDeAcesso=1,
                username=request.POST.get("username"),
                enderecoFuncionario=request.POST.get("enderecoFuncionario"),
                CPF=request.POST.get("CPF"),
                CEP=request.POST.get("CEP"),
                telefone=request.POST.get("telefone"),
                password=request.POST.get("password"),
                funcao=request.POST.get("funcao"),
                email=request.POST.get("email")
            )
            user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
            
            if user:
                funcionarios = Funcionario.objects.all()
                return redirect(Funcionarios)
            else:
                return HttpResponse(user)
def editar_view(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    return render(request, "update.html", {"funcionario": funcionario})
def update_view(request, id):
    if request.method == 'POST':
        funcionario = Funcionario.objects.get(idFuncionario=id)

        # Atualiza os campos do funcionário com base nos dados do formulário
        funcionario.username = request.POST.get("username")
        funcionario.enderecoFuncionario = request.POST.get("enderecoFuncionario")
        funcionario.CPF = request.POST.get("CPF")
        funcionario.CEP = request.POST.get("CEP")
        funcionario.telefone = request.POST.get("telefone")
        funcionario.email = request.POST.get("email")
        funcionario.funcao = request.POST.get("funcao")
        try:
            funcionario.full_clean()
        except ValidationError as e:
            return HttpResponse(f"Erro de validacao do formulário: {e}")
        funcionario.save()
        return redirect(Funcionarios)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
def delete_view(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(Funcionarios)