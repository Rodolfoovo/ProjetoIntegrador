from django.shortcuts import render, redirect
from .models import Produtos
from .forms import criaProdutoForm
from Fornecedores.models import Fornecedor
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.views import verifica_login, login_view
# Create your views here

def produtos_view(request):
    if(verifica_login(request)):
        produtos = Produtos.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request,"produtos.html", {"produtos": produtos, "fornecedores": fornecedores})
    else:
        return redirect(login_view)

def criaProdutos_view(request):
    if request.method == 'POST':
        if(verifica_login(request)):
            idFornecedor = request.POST.get("idFornecedor")
            fornecedor = Fornecedor.objects.get(idFornecedor=idFornecedor)

            vnomeProduto = request.POST.get("nomeProduto")
            vidFornecedor = fornecedor
            vvalorUnit = request.POST.get("valorUnit")
            vqntEstoque = request.POST.get("qntEstoque")
            vcategoria = request.POST.get("categoria")
            vsubCategoria = request.POST.get("subCategoria")
            vmarcaProduto = request.POST.get("marcaProduto")
            produto = Produtos.objects.create(
                idFornecedor = vidFornecedor,
                nomeProduto = vnomeProduto,
                valorUnit=vvalorUnit,
                qntEstoque=vqntEstoque,
                categoria=vcategoria,
                subCategoria=vsubCategoria,
                marcaProduto=vmarcaProduto)
    #        form = criaProdutoForm(request.POST)
    #        if form.is_valid():
    #            produtos = form.save(commit=False)
    #            produtos.save()
            return redirect(produtos_view)
        else:
            return redirect(login_view)
def editarProdutos_view(request, id):
    if(verifica_login(request)):
        produto =Produtos.objects.get(idProduto=id) 
        fornecedores = Fornecedor.objects.all()
        return render(request, "updateProduto.html", {"produto": produto, "fornecedores":fornecedores})
    else:
        return redirect(login_view)
def updateProdutos_view(request,id):
    if request.method == 'POST':
        if(verifica_login(request)):
            produtos = Produtos.objects.get(idProduto=id)
            idFornecedor = request.POST.get("idFornecedor")
            fornecedor = Fornecedor.objects.get(idFornecedor=idFornecedor)
    #        form = criaProdutoForm(request.POST,instance=produtos)
    #        if form.is_valid():
    #            form.save()
            produtos.nomeProduto = request.POST.get("nomeProduto")
            produtos.idFornecedor = fornecedor
            produtos.valorUnit = request.POST.get("valorUnit")
            produtos.qntEstoque = request.POST.get("qntEstoque")
            produtos.categoria = request.POST.get("categoria")
            produtos.subCategoria = request.POST.get("subCategoria")
            produtos.marcaProduto = request.POST.get("marcaProduto")

            produtos.save()
            return redirect(produtos_view)
        else:
            return redirect(login_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def deleteProduto_view(request, id):
    if(verifica_login(request)):
        produto = Produtos.objects.get(idProduto=id) 
        produto.delete()
        return redirect(produtos_view)
    else:
        return redirect(login_view)    