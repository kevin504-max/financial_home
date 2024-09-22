from django import forms
from .models import Gastos
from categoria.models import Categoria
from metodopagamento.models import MetodoPagamento
from recorrencia.models import Recorrencia
from usuarios.models import Usuario

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['descricao', 'valor', 'data', 'categoria', 'metodo_pagamento', 'recorrencia', 'usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), 
        }
    
    def __init__(self, *args, **kwargs):
        super(GastosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.all()
        self.fields['metodo_pagamento'].queryset = MetodoPagamento.objects.all()
        self.fields['recorrencia'].queryset = Recorrencia.objects.all()
        self.fields['usuario'].queryset = Usuario.objects.all()
        self.fields['data'].input_formats = ['%Y-%m-%d']
