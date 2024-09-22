from django.contrib import admin

from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nome') 

admin.site.register(Categoria, CategoriaAdmin)
