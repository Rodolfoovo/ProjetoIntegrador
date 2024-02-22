from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    idFornecedor = models.AutoField(primary_key=True)
    nomeFornecedor = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)