from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from collections import Counter
import calendar
from django.db.models import Count, Sum

from apps.clinica import models as modelsClinica
from apps.usuarios import models as modelsUsuario

# Create your views here.
class InicioTemplateView(TemplateView):
    template_name = 'inicio/index.html'

    def get(self, request):
        data={}
        inicio=True

        ultimos_seis_servicios = modelsClinica.Servicio.objects.filter(activo=True).order_by('-id')[:6]
        servicios = ultimos_seis_servicios
        hay_servicios=len(servicios)>0

        ultimos_seis_empleados = modelsUsuario.Perfil.objects.filter(activo=True).order_by('-id')[:6]
        empleados = ultimos_seis_empleados
        hay_empleados=len(empleados)>0

        data['hay_servicios'] = hay_servicios
        data['servicios'] = servicios

        data['hay_empleados']=hay_empleados
        data['empleados'] = empleados

        data['inicio']=inicio
        return render(request=request, template_name=self.template_name,context=data)
    
class ServiciosTemplateView(TemplateView):
    template_name = 'inicio/servicios.html'

    def get(self, request):
        data={}
        servicios = modelsClinica.Servicio.objects.all()
        hay_servicios=len(servicios)>0

        data['hay_servicios'] = hay_servicios
        data['servicios'] = servicios
        return render(request=request,template_name=self.template_name,context=data)
    
class NuestroEquipoTemplateView(TemplateView):
    template_name = 'inicio/nuestro_equipo.html'

    def get(self, request):
        return render(request=request,template_name=self.template_name)

class ContactoTemplateView(TemplateView):
    template_name = 'inicio/contacto.html'

    def get(self, request):
        return render(request=request,template_name=self.template_name)
    
class PanelTemplateView(TemplateView):
    template_name = 'panel.html'

    @method_decorator(login_required)
    def get(self, request):
        from apps.paciente import models as mPaciente
        from apps.clinica import models as mClinica
        # Datos generales
        total_pacientes = mPaciente.Paciente.objects.filter(activo=True).count()
        total_citas = mClinica.Cita.objects.filter(activo=True).count()

        # Obtener citas del año actual
        year_actual = datetime.now().year
        todas_las_citas = mClinica.Cita.objects.filter(activo=True, fecha__year=year_actual)

        # Filtrar citas pagadas y pendientes
        citas_pagadas = [cita for cita in todas_las_citas if cita.pagado()]
        citas_pendientes = [cita for cita in todas_las_citas if not cita.pagado()]
        citas_sin_pagar = [cita for cita in todas_las_citas if cita.pago_pendiente == cita.totalpago]

        # Conteo por mes
        conteo_por_mes = {mes: 0 for mes in range(1, 13)}  # Inicializa conteo para todos los meses

        for cita in todas_las_citas:
            mes = cita.fecha.month  # Obtener el mes de la fecha de la cita
            conteo_por_mes[mes] += 1  # Incrementar el conteo para ese mes

        # Asegurarse de que cada mes tenga un valor (0 si no hay)
        conteo_mensual = [conteo_por_mes[mes] for mes in range(1, 13)]

        # Contar estados de las citas
        estados = [cita.ESTADO_CHOICES[0][0], cita.ESTADO_CHOICES[1][0], cita.ESTADO_CHOICES[2][0], cita.ESTADO_CHOICES[3][0]]  # Lista de estados
        conteo_por_estado = {estado: 0 for estado in estados}

        # Contar citas por estado
        for cita in todas_las_citas:
            conteo_por_estado[cita.estado] += 1

        # Asegurarse de que cada estado tenga un valor (0 si no hay)
        conteo_por_estado = {estado: conteo_por_estado.get(estado, 0) for estado in estados}

        data = {
            'total_pacientes': total_pacientes,
            'total_citas': total_citas,
            'citas_pagadas': len(citas_pagadas),
            'citas_pendientes': len(citas_pendientes),
            'citas_sin_pagar': len(citas_sin_pagar),
            'estado_citas': todas_las_citas.values('estado').annotate(count=Count('id')),
            'conteo_por_estado': conteo_por_estado,
            'meses': [calendar.month_name[mes] for mes in range(1, 13)],
            'conteo_mensual': conteo_mensual,
        }

        
        return render(request=request,template_name=self.template_name,context=data)