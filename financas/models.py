from django.db import models

class Gastos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE, null=True)  
    metodo_pagamento = models.ForeignKey('metodopagamento.MetodoPagamento', on_delete=models.CASCADE, null=True)  
    recorrencia = models.ForeignKey('recorrencia.Recorrencia', on_delete=models.CASCADE, null=True)  
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, null=True)  

    def __str__(self):
        return self.descricao

