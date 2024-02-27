from django.shortcuts import render, redirect
from .models import Produtos
from .forms import criaProdutoForm
from django.http import HttpResponse
# Create your views here.
def produtos_view(request):
    produtos = Produtos.objects.all()
    produtoForm = criaProdutoForm()
    return render(request,"produtos.html", {"produtos": produtos, 'produtoForm':produtoForm})

def criaProdutos_view(request):
    if request.method == 'POST':
        vnomeProduto = request.POST.get("username")
        vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
        vCPF = request.POST.get("CPF")
        vCEP = request.POST.get("CEP")
        vTelefone = request.POST.get("telefone")
        vpassword = request.POST.get("password")
        vFuncao = request.POST.get("funcao")
        vEmail = request.POST.get("email")
#        form = criaProdutoForm(request.POST)
#        if form.is_valid():
#            produtos = form.save(commit=False)
#            produtos.save()
        return redirect(produtos_view)
def editarProdutos_view(request, id):
    produto =Produtos.objects.get(idProduto=id) 
    return render(request, "updateProduto.html", {"produto": produto})

def updateProdutos_view(request,id):
    if request.method == 'POST':
        produtos = Produtos.objects.get(idProduto=id)
        form = criaProdutoForm(request.POST,instance=produtos)
        if form.is_valid():
            form.save()
            return redirect(produtos_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def deleteProduto_view(request, id):
    produto = Produtos.objects.get(idPRoduto=id) 
    produto.delete()
    return redirect(produtos_view)
    