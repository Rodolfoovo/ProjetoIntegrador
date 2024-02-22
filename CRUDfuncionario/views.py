from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse
from django.core.exceptions import ValidationError

def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "index.html", {"funcionarios": funcionarios})

def salvarFuncionario_view(request):
    if request.method == 'GET':
        return render(request, "index.html")
    elif request.method == 'POST':
        vusername = request.POST.get("username")
        vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
        vCPF = request.POST.get("CPF")
        vCEP = request.POST.get("CEP")
        vTelefone = request.POST.get("telefone")
        vpassword = request.POST.get("password")
        vFuncao = request.POST.get("funcao")
        vEmail = request.POST.get("email")
        if validar_cpf(vCPF) != True:
            raise ValidationError('CPF invalido')
        # Verifica se já existe um usuário com o mesmo username
        try:
            usuarioAux = Funcionario.objects.get(username=vusername)
            return redirect(home)
        except Funcionario.DoesNotExist:
            # Cria um novo usuário
            novo_funcionario = Funcionario.objects.create_user(
                nivelDeAcesso=1,
                username=vusername,
                enderecoFuncionario=vEnderecoFuncionario,
                cpf=vCPF,
                CEP=vCEP,
                telefone=vTelefone,
                password=vpassword,
                funcao=vFuncao,
                email=vEmail
            )

            # Autentica o novo usuário
            user = authenticate(request, username=vusername, password=vpassword)
            
            if user:
                funcionarios = Funcionario.objects.all()
                return redirect(home)
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

        funcionario.save()
        return redirect(home)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def delete_view(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(home)
def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    # Verifica se os dígitos verificadores são iguais aos dois últimos dígitos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"