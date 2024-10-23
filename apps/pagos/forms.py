from django import forms
from .models import ControlPago

class ControlPagoForm(forms.ModelForm):
    class Meta:
        model = ControlPago
        fields = ['cantidadpago', 'descripcion', 'tipopago', 'numref', 'cita']
        widgets = {
            'cantidadpago': forms.NumberInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'style': 'border: 1px solid'}),
            'tipopago': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'numref': forms.TextInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'cita': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
        }