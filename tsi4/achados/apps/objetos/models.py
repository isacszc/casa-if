from pyexpat import model
from django.db import models

class Tipo_Objeto(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Objeto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    local = models.CharField('Local', max_length=200)
    data_hora = models.DateTimeField('Data e Hora')
    tipo_objeto = models.ForeignKey(Tipo_Objeto, on_delete=models.PROTECT)