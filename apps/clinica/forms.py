from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreservicio', 'descripcion', 'costo']
        widgets = {
            'nombreservicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre','style': 'border: 1px solid'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descipción','rows':'5','cols':'50','style':'resize:none;border: 1px solid'}),
            'costo': forms.TextInput(attrs={'class': 'form-control', 'type': 'number','style': 'border: 1px solid'}),
        }
