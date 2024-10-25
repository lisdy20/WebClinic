from django import forms
from .models import ExInterno

class ExamenInternoForm(forms.ModelForm):
    class Meta:
        model = ExInterno
        fields = ['detallecita', 'motivo', 'nombredoctor']
        widgets = {
            'detallecita': forms.Select(attrs={'class': 'form-control','style':'border:1px solid'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control','style':'border:1px solid'}),
            'nombredoctor': forms.TextInput(attrs={'class': 'form-control','style':'border:1px solid'}),
        }