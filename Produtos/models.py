from django.db import models
from Fornecedores.models import Fornecedor
from django.core.exceptions import ValidationError
# Create your models here.

class Produtos(models.Model):
   idProduto = models.AutoField(primary_key=True)
   idFornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
   nomeProduto=models.CharField(max_length= 30)
   valorUnit= models.DecimalField(max_digits=10,decimal_places=2)
   qntEstoque =models.IntegerField(default = 1)
   categoria = models.CharField(max_length=15)
   subCategoria=models.CharField(max_length=15)
   marcaProduto=models.CharField(max_length=15)

   def validar_dados(self,produto):
      try:
         produto.full_clean()
         return True
      except ValidationError:
         return False