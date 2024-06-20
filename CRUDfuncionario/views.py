from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
@login_required
def Funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "funcionarios.html", {"funcionarios": funcionarios})
@login_required
def salvarFuncionario_view(request):
    if request.method == 'GET':
        return render(request, "funcionarios.html")
    elif request.method == 'POST':
        vusername = request.POST.get("username")
        vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
        vCPF = request.POST.get("CPF")
        vCEP = request.POST.get("CEP")
        vTelefone = request.POST.get("telefone")
        vpassword = request.POST.get("password")
        vFuncao = request.POST.get("funcao")
        vEmail = request.POST.get("email")
 
        # Verifica se já existe um usuário com o mesmo username
        try:
            usuarioAux = Funcionario.objects.get(username=vusername)
            return redirect(Funcionarios)
        except Funcionario.DoesNotExist:
            # Cria um novo usuário
            novo_funcionario = Funcionario(
                nivelDeAcesso=1,
                username=vusername,
                enderecoFuncionario=vEnderecoFuncionario,
                CPF=vCPF,
                CEP=vCEP,
                telefone=vTelefone,
                password=vpassword,
                funcao=vFuncao,
                email=vEmail
            )
            try:
                novo_funcionario.full_clean()
            except ValidationError as e:
                return HttpResponse(f"Erro de validacao do formulário: {e}")
            # Autentica o novo usuário
            novo_funcionario =Funcionario.objects.create_user(
                nivelDeAcesso=1,
                username=vusername,
                enderecoFuncionario=vEnderecoFuncionario,
                CPF=vCPF,
                CEP=vCEP,
                telefone=vTelefone,
                password=vpassword,
                funcao=vFuncao,
                email=vEmail
            )
            user = authenticate(request, username=vusername, password=vpassword)
            
            if user:
                funcionarios = Funcionario.objects.all()
                return redirect(Funcionarios)
            else:
                return HttpResponse(user)
@login_required
def editar_view(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    return render(request, "update.html", {"funcionario": funcionario})
@login_required
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
        try:
            funcionario.full_clean()
        except ValidationError as e:
            return HttpResponse(f"Erro de validacao do formulário: {e}")
        funcionario.save()
        return redirect(Funcionarios)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
login_required
def delete_view(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(Funcionarios)
