from django.contrib import admin

from .models import MetodoPagamento

class MetodoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')

admin.site.register(MetodoPagamento, MetodoPagamentoAdmin)


