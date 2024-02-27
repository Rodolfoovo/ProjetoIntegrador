from django.shortcuts import render
from .models import Fornecedor
from .forms import FornecedorForm
from django.shortcuts import redirect
from django.http import HttpResponse
import re
# Create your views here.

def fornecedor_view(request):
    fornecedores = Fornecedor.objects.all()
    fornecedorForm = FornecedorForm()
    return render(request,"fornecedor.html",{"fornecedores":fornecedores, 'fornecedorForm': fornecedorForm})

def salvarFornecedor_view(request):
    if request.method == 'POST':
#        form = FornecedorForm(request.POST)
        vnomeFornecedor = request.POST.get("nomeFornecedor")
        vendereco = request.POST.get("endereco")
        vtelefone = request.POST.get("telefone")
        vcep = request.POST.get("cep")
        vcnpj = request.POST.get("cnpj")
        fornecedor = Fornecedor.objects.create(
            nomeFornecedor=vnomeFornecedor,
            endereco=vendereco,
            telefone=vtelefone,
            cep=vcep,
            cnpj=vcnpj)
#        if form.is_valid():
#            fornecedor = form.save(commit=False)

#            fornecedor.save()
        return redirect(fornecedor_view)
def editarFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    return render(request, "updateFornecedor.html", {"Fornecedor": fornecedor})

def updateFornecedor_view(request,id):
    if request.method == 'POST':
        fornecedor = Fornecedor.objects.get(idFornecedor=id)
        fornecedor.nomeFornecedor = request.POST.get("nomeFornecedor")
        fornecedor.endereco = request.POST.get("endereco")
        fornecedor.telefone = request.POST.get("telefone")
        fornecedor.cep = request.POST.get("cep")
        fornecedor.cnpj = request.POST.get("cnpj")
#        form = FornecedorForm(request.POST, instance=fornecedor)
#        if form.is_Valid():
#            form.save()
#            return redirect(fornecedor_view)
#    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
#        return HttpResponse('Método não permitido')
        return redirect(fornecedor_view)
    
def deleteFornecedor_view(request, id):
    fornecedor = Fornecedor.objects.get(idFornecedor=id) 
    fornecedor.delete()
    return redirect(fornecedor_view)

def valida_cnpj(cnpj):
    #Função para validar o cnpj, será aplicada em trabalhos futuros
    cnpj = ''.join(re.findall('\\d', str(cnpj)))

    if (len(cnpj) != 14):
        return False

    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    if novo == inteiros:
        return True

    return False

def valida_cep(cep):
    # A função re.match tenta combinar a string fornecida com a expressão regular
    # A expressão regular r'^\d{5}-\d{3}$' corresponde a uma string que começa (^) com 5 dígitos (\d{5}), seguida por um hífen (-), e termina ($) com 3 dígitos (\d{3})
    # Se a string do CEP combinar com essa expressão regular, a função re.match retornará um objeto de correspondência, caso contrário, retornará None
    # O operador 'is not None' verifica se o resultado da função re.match é diferente de None, ou seja, se houve uma correspondência
    # Portanto, a função valida_cep retorna True se o CEP estiver no formato correto e False caso contrário
    return re.match(r'^\d{5}-\d{3}$', cep) is not None


