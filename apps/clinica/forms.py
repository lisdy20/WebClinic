from apps.common import forms
from .models import (
    Servicio,
    Cita
    )

class ServicioForm(forms.GenericForm):
    class Meta:
        model = Servicio
        fields = ['nombreservicio', 'descripcion', 'costo']

class CitaForm(forms.GenericForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'paciente', 'numaut', 'numserie', 'dte', 'facturado', 'estadocita', 'totalpago', 'totalpagado', 'perfil', 'recetamedica']
        
