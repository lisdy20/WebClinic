from apps.common import forms
from .models import (
    Servicio,
    DetalleCita,
    Cita
    )

class ServicioForm(forms.GenericForm):
    class Meta:
        model = Servicio
        fields = ['nombreservicio', 'descripcion', 'costo']

class CitaForm(forms.GenericForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'paciente','numaut','numserie', 'dte', 'facturado', 'estado','totalpago', 'totalpagado','perfil','recetamedica']


class DetalleCitaForm(forms.GenericForm):
    class Meta:
        model = DetalleCita
        fields = ['servicio','descuento','cita']  # Include all fields
        
