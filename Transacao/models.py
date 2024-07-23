from django.db import models
from django.core.exceptions import ValidationError
from Fornecedores.models import Fornecedor
# Create your models here.

class Transacao(models.Model):
    idTransacao = models.AutoField(primary_key=True)
    idFornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE, default=1)
    dataTransacao = models.DateField()
    tipoTransacao = models.CharField(max_length=7)

    def validar_dados(self,produto):
      try:
         produto.full_clean()
         return True
      except ValidationError:
         return False

    