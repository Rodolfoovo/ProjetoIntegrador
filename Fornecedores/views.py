from django.shortcuts import render
from .models import Fornecedor
from .forms import FornecedorForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import re
# Create your views here.

def fornecedor_view(request):
    fornecedores = Fornecedor.objects.all()
    fornecedorForm = FornecedorForm()
    return render(request,"fornecedor.html",{"fornecedores":fornecedores, 'fornecedorForm': fornecedorForm})

def salvarFornecedor_view(request):
    if request.method == 'POST':
#        form = FornecedorForm(request.POST)
        fornecedor = Fornecedor(
            nomeFornecedor=request.POST.get("nomeFornecedor"),
            endereco=request.POST.get("endereco"),
            telefone=request.POST.get("telefone"),
            cep=request.POST.get("cep"),
            cnpj=request.POST.get("cnpj"))
        try:
            fornecedor.full_clean()
        except ValidationError as e:
            return HttpResponse(f"Erro de validacao do formulário: {e}")
        fornecedor = Fornecedor.objects.create(
            nomeFornecedor=request.POST.get("nomeFornecedor"),
            endereco=request.POST.get("endereco"),
            telefone=request.POST.get("telefone"),
            cep=request.POST.get("cep"),
            cnpj=request.POST.get("cnpj")
            )
        fornecedor.save()
        return redirect(fornecedor_view)
def editarFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    return render(request, "updateFornecedor.html", {"fornecedor": fornecedor})

def updateFornecedor_view(request,id):
    if request.method == 'POST':
        fornecedor = Fornecedor.objects.get(idFornecedor=id)
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
    
def deleteFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    fornecedor.delete()
    return redirect(fornecedor_view)


