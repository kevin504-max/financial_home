from django import forms
from .models import Recorrencia

class RecorrenciaForm(forms.ModelForm):
    class Meta:
        model = Recorrencia
        fields = ['nome', 'intervalo']