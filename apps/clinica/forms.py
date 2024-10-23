from django import forms
from .models import (
    Servicio,
    Cita
    )

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreservicio', 'descripcion', 'costo']
        widgets = {
            'nombreservicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre','style': 'border: 1px solid'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descipción','rows':'5','cols':'50','style':'resize:none;border: 1px solid'}),
            'costo': forms.TextInput(attrs={'class': 'form-control', 'type': 'number','style': 'border: 1px solid'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'paciente', 'numaut', 'numserie', 'dte', 'facturado', 'estadocita', 'totalpago', 'totalpagado', 'perfil', 'recetamedica']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local','style': 'border: 1px solid'}),
            'paciente': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'numaut': forms.TextInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'numserie': forms.TextInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'dte': forms.TextInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'facturado': forms.CheckboxInput(attrs={'class': 'form-check-input','style': 'border: 1px solid'}),
            'estadocita': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'totalpago': forms.NumberInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'totalpagado': forms.NumberInput(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'perfil': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
            'recetamedica': forms.Select(attrs={'class': 'form-control','style': 'border: 1px solid'}),
        }
