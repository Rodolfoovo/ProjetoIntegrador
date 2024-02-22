from django.shortcuts import render
from .models import Fornecedor
from .forms import FornecedorForm
from django.shortcuts import redirect
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
