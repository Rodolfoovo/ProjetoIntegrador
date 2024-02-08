from django.shortcuts import render

def Produtos(request):
    return render(request, 'Produtos.html')