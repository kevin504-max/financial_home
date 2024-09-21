from django.contrib import admin

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email')

admin.site.register(Usuario, UsuarioAdmin)

