from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    idFornecedor = models.AutoField(primary_key=True)
    nomeFornecedor = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)

class Produtos(models.Model):
   idProduto = models.AutoField(primary_key=True)
   idFornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
   nomeProduto=models.CharField(max_length= 30)
   valorUnit= models.DecimalField(max_digits=10,decimal_places=2)
   qntEstoque =models.IntegerField(default = 1)
   categoria = models.CharField(max_length=15)
   subCategoria=models.CharField(max_length=15)
   marcaProduto=models.CharField(max_length=15)