from django import forms
from .models import MetodoPagamento

class MetodoPagamentoForm(forms.ModelForm):
    class Meta:
        model = MetodoPagamento
        fields = ['nome', 'descricao']
