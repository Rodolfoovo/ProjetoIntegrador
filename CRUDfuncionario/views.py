from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse

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

        # Verifica se já existe um usuário com o mesmo username
        try:
            usuarioAux = Funcionario.objects.get(username=vusername)
            return render(request, "index.html", {'msg': 'Erro! Já existe este nome no sistema'})
        except Funcionario.DoesNotExist:
            # Cria um novo usuário
            novo_funcionario = Funcionario.objects.create(
                nivelDeAcesso=1,
                username=vusername,
                enderecoFuncionario=vEnderecoFuncionario,
                CPF=vCPF,
                CEP=vCEP,
                telefone=vTelefone,
                password=vpassword,
                funcao=vFuncao
            )

            # Autentica o novo usuário
            user = authenticate(request, username=vusername, password=vpassword)
            if user is not None:
                login(request, user)
                return HttpResponse('Usuário cadastrado e autenticado com sucesso.')
            else:
                return HttpResponse('Erro ao autenticar o usuário.')

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
        funcionario.password = request.POST.get("password")
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
