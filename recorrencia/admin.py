from django.contrib import admin

from .models import Recorrencia

class RecorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'intervalo')

admin.site.register(Recorrencia, RecorrenciaAdmin)
