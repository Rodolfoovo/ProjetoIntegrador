from django.db import models

# Create your models here.

class Produtos(models.Model):
    idProduto = models.AutoField(primary_key=True)
    valorUnit= models.IntegerField(default = 1)
    qntEstoque =models.IntegerField(default = 1)
    nomeProduto=models.CharField(max_length= 30)
    categoria = models.CharField(max_length=15)
    subCategoria=models.CharField(max_length=15)
    marcaProduto=models.CharField(max_length=15)