from django.shortcuts import render
from .models import Produtos
# Create your views here.
def produtos_view(request):
    produtos = Produtos.objects.all()
    return render(request,"produtos.html", {"produtos": produtos})