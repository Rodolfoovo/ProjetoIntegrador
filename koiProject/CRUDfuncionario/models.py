from django.db import models

# Create your models here.
class Funcionario(models.Model):
    idFuncionario = models.AutoField(primary_key=True)
    nivelDeAcesso = models.IntegerField()
    nomeFuncionario = models.CharField(max_length=30)
    enderecoFuncionario = models.CharField(max_length=30)
    CPF = models.CharField(max_length=11)
    CEP = models.CharField(max_length=8)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)

    def __str__(self):
        return self.nomeFuncionario