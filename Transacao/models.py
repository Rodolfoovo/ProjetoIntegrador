from django.db import models

# Create your models here.

class Transacao(models.Model):
    idTransacao = models.AutoField(primary_key=True)
    dataTransacao = models.DateField()
    tipoTransacao = models.CharField(max_length=7)