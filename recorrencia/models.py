from django.db import models

class Recorrencia(models.Model):
    nome = models.CharField(max_length=100)
    intervalo = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
