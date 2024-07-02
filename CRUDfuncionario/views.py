from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from login.views import login_view, verifica_login

def Funcionarios(request):
    if verifica_login(request):
        funcionarios = Funcionario.objects.all()
        return render(request, "funcionarios.html", {"funcionarios": funcionarios})
    else:
        return redirect(login_view)

def cadastrarFuncionario_view(request):
    if request.method == 'POST':
        if verifica_login(request):
            username = request.POST.get("username")
            try:
                usuarioAux = Funcionario.objects.get(username=username)
                return HttpResponse(f"Já existe um funcionário com o username '{username}'")
            except Funcionario.DoesNotExist:
                funcionario_instance = Funcionario(
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
                novo_funcionario = funcionario_instance.criar_usuario(funcionario_instance)
                user = funcionario_instance.autenticar(request,username, funcionario_instance.password)
                if user:
                    return redirect(Funcionarios)
                else:
                    return HttpResponse("Falha na autenticação do usuário")
        else:
            return redirect(login_view)
    else:
        return render(request, "cadastrarFuncionario.html")

def editarFuncionario_view(request, id):
    if verifica_login(request):
        funcionario = Funcionario.objects.get(idFuncionario=id)
        return render(request, "updateFuncionario.html", {"funcionario": funcionario})
    else:
        return redirect(login_view)

def updateFuncionario_view(request, id):
    if request.method == 'POST':
        if verifica_login(request):
            funcionario = Funcionario.objects.get(idFuncionario=id)

            # Atualiza os campos do funcionário com base nos dados do formulário
            funcionario.username = request.POST.get("username")
            funcionario.enderecoFuncionario = request.POST.get("enderecoFuncionario")
            funcionario.CPF = request.POST.get("CPF")
            funcionario.CEP = request.POST.get("CEP")
            funcionario.telefone = request.POST.get("telefone")
            funcionario.email = request.POST.get("email")
            funcionario.funcao = request.POST.get("funcao")
            funcionario.validar_dados(funcionario)
            funcionario.save()
            return redirect(Funcionarios)
        else:
            return redirect(login_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')

def deleteFuncionario_view(request, id):
    if verifica_login(request):
        funcionario = Funcionario.objects.get(idFuncionario=id)
        funcionario.delete()
        return redirect(Funcionarios)
    else:
        return redirect(login_view)
