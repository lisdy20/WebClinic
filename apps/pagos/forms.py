from apps.common import forms
from .models import ControlPago

class ControlPagoForm(forms.GenericForm):
    class Meta:
        model = ControlPago
        fields = ['cantidadpago', 'descripcion', 'tipopago', 'numref', 'cita']