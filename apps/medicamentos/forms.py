from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['medicamento', 'descripcion']
        widgets = {
            'medicamento': forms.TextInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'style': 'border: 1px solid'}),
        }