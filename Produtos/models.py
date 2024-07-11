from django.db import models
from datetime import date, timedelta, datetime
from Fornecedores.models import Fornecedor
from django.core.exceptions import ValidationError
from Transacao.models import Transacao
import calendar
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
      
from datetime import date

def calcular_estoque_total():
    # Obtém todos os produtos da tabela
    produtos = Produtos.objects.all()

    # Inicializa o estoque total como zero
    estoque_total = 0
    hoje = date.today
    inicio = date(hoje.year, hoje.month, 1)  # Data de início do período
    fim = date(hoje.year,hoje.month, calendar.calendar_monthrange(hoje.today,hoje.month)[1])  # Data de fim do período
    # Itera sobre cada produto e adiciona sua quantidade de estoque ao total
    for produto in produtos:
        # Obtém a transação associada ao produto dentro do período especificado
        try:
            transacao = Transacao.objects.get(idTransacao=produto.idTransacao, dataTransacao__range=(inicio, fim))
            if transacao.tipoTransacao == "Entrada":
                estoque_total += produto.qntEstoque*produto.valorUnit
            else:
                estoque_total -= produto.qntEstoque*produto.valorUnit
        except Transacao.DoesNotExist:
            # Caso não haja transação associada, trata como erro ou define um comportamento padrão
            pass

    return estoque_total


