from django import forms
from .models import Produtos, Fornecedor  # Importe o modelo associado

class criaProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nomeProduto','idFornecedor', 'valorUnit', 'qntEstoque', 'categoria', 'subCategoria', 'marcaProduto']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nomeFornecedor','endereco','telefone','cep','cnpj']