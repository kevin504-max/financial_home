from django.db import models

class Gastos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE, null=True)  # Permite valores nulos
    metodo_pagamento = models.ForeignKey('metodopagamento.MetodoPagamento', on_delete=models.CASCADE, null=True)  # Permite valores nulos
    recorrencia = models.ForeignKey('recorrencia.Recorrencia', on_delete=models.CASCADE, null=True)  # Permite valores nulos
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, null=True)  # Permite valores nulos

    def __str__(self):
        return self.descricao

# Create your models here.
