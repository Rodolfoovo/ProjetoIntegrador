from django.shortcuts import render
from .models import Produtos
from .forms import criaProdutoForm
# Create your views here.
def produtos_view(request):
    produtos = Produtos.objects.all()
    produtoForm = criaProdutoForm()
    return render(request,"produtos.html", {"produtos": produtos, 'produtoForm':produtoForm})


    