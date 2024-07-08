from django.shortcuts import render
from .models import Fornecedor
from .forms import FornecedorForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from login.views import verifica_login, login_view
import re
# Create your views here.

def fornecedor_view(request):
    if(verifica_login(request)):
        fornecedores = Fornecedor.objects.all()
        fornecedorForm = FornecedorForm()
        return render(request,"fornecedor.html",{"fornecedores":fornecedores, 'fornecedorForm': fornecedorForm})
    else:
        return redirect(login_view)

def salvarFornecedor_view(request):
    if request.method == 'POST':
        if(verifica_login(request)):
    #        form = FornecedorForm(request.POST)
            fornecedor = Fornecedor(
                nomeFornecedor=request.POST.get("nomeFornecedor"),
                endereco=request.POST.get("endereco"),
                telefone=request.POST.get("telefone"),
                cep=request.POST.get("cep"),
                cnpj=request.POST.get("cnpj"))
            if(fornecedor.validar_dados(fornecedor) == False):
                return HttpResponse("Erro nos dados inseridos!")
            fornecedor = Fornecedor.objects.create(
                nomeFornecedor=request.POST.get("nomeFornecedor"),
                endereco=request.POST.get("endereco"),
                telefone=request.POST.get("telefone"),
                cep=request.POST.get("cep"),
                cnpj=request.POST.get("cnpj")
                )
            fornecedor.save()
            return redirect(fornecedor_view)
        else:
            return redirect(login_view)

def cadastrarFornecedor_view(request):
    if request.method == 'POST':
        if(verifica_login(request)):
    #        form = FornecedorForm(request.POST)
            fornecedor = Fornecedor(
                nomeFornecedor=request.POST.get("nomeFornecedor"),
                endereco=request.POST.get("endereco"),
                telefone=request.POST.get("telefone"),
                cep=request.POST.get("cep"),
                cnpj=request.POST.get("cnpj"))
            if(fornecedor.validar_dados(fornecedor) == False):
                return HttpResponse("Erro nos dados inseridos!")
            fornecedor = Fornecedor.objects.create(
                nomeFornecedor=request.POST.get("nomeFornecedor"),
                endereco=request.POST.get("endereco"),
                telefone=request.POST.get("telefone"),
                cep=request.POST.get("cep"),
                cnpj=request.POST.get("cnpj")
                )
            fornecedor.save()
            return redirect(fornecedor_view)
        else:
            return redirect(login_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return render(request,"cadastrarFornecedor.html ")

def editarFornecedor_view(request, id):
    if(verifica_login(request)):
        fornecedor = fornecedor_existe(id)
        return render(request, "updateFornecedor.html", {"fornecedor": fornecedor})
    else:
        redirect(login_view)

def updateFornecedor_view(request,id):
    if request.method == 'POST':
        if(verifica_login(request)):
            fornecedor = fornecedor_existe(id)
            fornecedor.nomeFornecedor = request.POST.get("nomeFornecedor")
            fornecedor.endereco = request.POST.get("endereco")
            fornecedor.telefone = request.POST.get("telefone")
            fornecedor.cep = request.POST.get("cep")
            fornecedor.cnpj = request.POST.get("cnpj")
            try:
                fornecedor.full_clean()
            except ValidationError as e:
                return HttpResponse(f"Erro de validacao do formulário: {e}")
            fornecedor.save()
            return redirect(fornecedor_view)
        else:
            return redirect(login_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def deleteFornecedor_view(request, id):
    if(verifica_login(request)):
        fornecedor = fornecedor_existe(id)
        fornecedor.delete()
        return redirect(fornecedor_view)
    else:
        return redirect(login_view)
def fornecedor_existe(id):
    try:
        fornecedor = Fornecedor.objects.get(idFornecedor= id)
        return fornecedor
    except Fornecedor.DoesNotExist:
        return None