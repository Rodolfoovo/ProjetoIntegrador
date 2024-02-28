from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from .validators import valida_texto
# Create your models here.
class Funcionario(AbstractUser):
    idFuncionario = models.AutoField(primary_key=True)
    nivelDeAcesso = models.IntegerField(default=1)
    enderecoFuncionario = models.CharField(max_length=30)
#    CPF = models.CharField(max_length=11)
    CPF = CPFField('CPF',default='000.000.000-0')
    CEP = models.CharField(max_length=8)
    telefone = models.CharField(max_length=20)
    funcao = models.CharField(max_length=30)

    username = models.CharField(max_length=30,default='default_username', unique=True,
                                validators=[valida_texto])
    password = models.CharField(max_length=100, default='default_password')
    email = models.EmailField(unique=True, default='daniel@gmail.com', 
                              validators = [EmailValidator(message="Insira um endereco de email valído")])

    def __str__(self):
        return self.username