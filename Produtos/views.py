from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from Fornecedores.models import Fornecedor
from django.contrib.auth.decorators import login_required
from login.views import verifica_login, login_view

def produtos_view(request):
    produtos = Produtos.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, "produtos.html", {"produtos": produtos, "fornecedores": fornecedores})

def cadastrarProdutos_view(request):
    if request.method == 'POST':
        idFornecedor = request.POST.get("idFornecedor")
        fornecedor = get_object_or_404(Fornecedor, idFornecedor=idFornecedor)

        produto = Produtos(
            idFornecedor=fornecedor,
            nomeProduto=request.POST.get("nomeProduto"),
            valorUnit=request.POST.get("valorUnit"),
            qntEstoque=request.POST.get("qntEstoque"),
            categoria=request.POST.get("categoria"),
            subCategoria=request.POST.get("subCategoria"),
            marcaProduto=request.POST.get("marcaProduto")
        )
        if(produto.validar_dados(produto) == False):
            return HttpResponse("Erro nos dados inseridos!")
        produto = Produtos.objects.create(
            idFornecedor=fornecedor,
            nomeProduto=request.POST.get("nomeProduto"),
            valorUnit=request.POST.get("valorUnit"),
            qntEstoque=request.POST.get("qntEstoque"),
            categoria=request.POST.get("categoria"),
            subCategoria=request.POST.get("subCategoria"),
            marcaProduto=request.POST.get("marcaProduto")
        )
        produto.save()
        return redirect('produtos_view')
    else:
        fornecedores = Fornecedor.objects.all()
        return render(request, "cadastrarProdutos.html", {"fornecedores": fornecedores})

def editarProdutos_view(request, id):
    produto = get_object_or_404(Produtos, idProduto=id)
    fornecedores = Fornecedor.objects.all()
    return render(request, "updateProduto.html", {"produto": produto, "fornecedores": fornecedores})

def updateProdutos_view(request, id):
    if request.method == 'POST':
        produtos = get_object_or_404(Produtos, idProduto=id)
        idFornecedor = request.POST.get("idFornecedor")
        fornecedor = get_object_or_404(Fornecedor, idFornecedor=idFornecedor)

        produtos.nomeProduto = request.POST.get("nomeProduto")
        produtos.idFornecedor = fornecedor
        produtos.valorUnit = request.POST.get("valorUnit")
        produtos.qntEstoque = request.POST.get("qntEstoque")
        produtos.categoria = request.POST.get("categoria")
        produtos.subCategoria = request.POST.get("subCategoria")
        produtos.marcaProduto = request.POST.get("marcaProduto")
        if(produtos.validar_dados(produtos) == False):
            return HttpResponse("Erro nos dados inseridos!")
        produtos.save()
        return redirect('produtos_view')
    else:
        return HttpResponse('Método não permitido')

def deleteProduto_view(request, id):
    produto = get_object_or_404(Produtos, idProduto=id)
    produto.delete()
    return redirect('produtos_view')
