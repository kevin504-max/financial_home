from django import forms
from .models import Recorrencia

class RecorrenciaForm(forms.ModelForm):
    intervalo = forms.CharField(required=False)
    class Meta:
        model = Recorrencia
        fields = ['nome', 'intervalo']

    def clean_intervalo(self):
        intervalo = self.cleaned_data.get('intervalo')
        if intervalo == '':
            return None  
        return intervalo