from django.contrib import admin

from .models import Gastos

class GastosAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','valor','data','metodo_pagamento','categoria','recorrencia','usuario')

admin.site.register(Gastos, GastosAdmin)
