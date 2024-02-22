from django.shortcuts import render
from .models import Produtos, Fornecedor
from .forms import criaProdutoForm, FornecedorForm
# Create your views here.
def produtos_view(request):
    produtos = Produtos.objects.all()
    produtoForm = criaProdutoForm()
    return render(request,"produtos.html", {"produtos": produtos, 'produtoForm':produtoForm})

def fornecedor_view(request):
    fornecedores = Fornecedor.objects.all()
    fornecedorForm = FornecedorForm()
    return render(request,"fornecedor.html",{"fornecedores":fornecedores, 'fornecedorForm': fornecedorForm})
    