from django import forms
from .models import Produtos  # Importe o modelo associado

class criaProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nomeProduto', 'valorUnit', 'qntEstoque', 'categoria', 'subCategoria', 'marcaProduto']