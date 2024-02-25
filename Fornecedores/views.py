from django.shortcuts import render
from .models import Fornecedor
from .forms import FornecedorForm
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def fornecedor_view(request):
    fornecedores = Fornecedor.objects.all()
    fornecedorForm = FornecedorForm()
    return render(request,"fornecedor.html",{"fornecedores":fornecedores, 'fornecedorForm': fornecedorForm})

def salvarFornecedor_view(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save(commit=False)

            fornecedor.save()
            return redirect(fornecedor_view)
def editarFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    return render(request, "updateFornecedor.html", {"Fornecedor": fornecedor})

def updateFornecedor_view(request,id):
    if request.method == 'POST':
        fornecedor = Fornecedor.objects.get(idFornecedor=id)
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_Valid():
            form.save()
            return redirect(fornecedor_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def deleteFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    fornecedor.delete()
    return redirect(fornecedor_view)