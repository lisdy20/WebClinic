from django.db import models
from datetime import datetime
from apps.paciente.models import Paciente
from apps.usuarios.models import Perfil
from apps.medicamentos.models import RecetaMedica

# Create your models here.
class EstadoCita(models.Model):
    NombreEstado = models.CharField(max_length=30, db_column='NombreEstado', verbose_name='Estado de cita', blank=True, null=True)

    class Meta: 
        verbose_name = 'Estado de cita'
        verbose_name_plural = 'Estado de citas'
        db_table = 'EstadoCita'

class Historial(models.Model):
    motivo = models.CharField(max_length=80, db_column='motivo', verbose_name='Motivo de cita', blank=True, null=True)
    historiaenfer = models.CharField(max_length=80, db_column='historiaenfer', verbose_name='Historia de enfermedad', blank=True, null=True)
    presionarterial = models.CharField(max_length=20, db_column='presionarterial', verbose_name='Presión arterial', blank=True, null=True)
    frecuenciacard = models.CharField(max_length=5, db_column='frecuenciiacard', verbose_name='Frecuencia cardíaca', blank=True, null=True)
    frecuenciaresp = models.CharField(max_length=5, db_column='frecuenciaresp', verbose_name='Frecuencia respiratoria', blank=True, null=True)
    temperatura = models.CharField(max_length=5, db_column='temperatura', verbose_name='Temperatura', blank=True, null=True)
    saturacion = models.CharField(max_length=5, db_column='saturacion', verbose_name='Saturación', blank=True, null=True)
    glucosa = models.CharField(max_length=5, db_column='glucosa', verbose_name='Glucosa', blank=True, null=True)
    peso = models.CharField(max_length=5, db_column='peso', verbose_name='Peso', blank=True, null=True)
    altura = models.CharField(max_length=5, db_column='altura', verbose_name='Altura', blank=True, null=True)
    diagnostico = models.CharField(max_length=80, db_column='diagnostico', verbose_name='Diagnóstico', blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente_id', verbose_name='Paciente', blank=False, null=False)

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'
        db_table = 'Historial'

class Servicio(models.Model):
    nombreservicio = models.CharField(max_length=30, db_column='nombreservicio', verbose_name='Nombre del servicio', blank=False, null=False)
    descripcion = models.CharField(max_length=80, db_column='descripcion', verbose_name='Descripción del servicio', blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, db_column='costo', verbose_name='Costo del servicio', blank=False, null=False)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'Servicio'

class Cita(models.Model):
    fecha = models.DateTimeField(default=datetime.now(), db_column='fecha', verbose_name='Fecha de cita', blank=False, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente_id', verbose_name='Paciente', blank=False, null=False)
    numaut = models.CharField(max_length=80, db_column='numaut', verbose_name='Número de autorización', blank=False, null=False)
    numserie = models.CharField(max_length=80, db_column='numserie', verbose_name='Número de serie', blank=False, null=False)
    dte = models.CharField(max_length=80, db_column='dte', verbose_name='DTE', blank=False, null=False)
    facturado = models.BooleanField(db_column='facturado', verbose_name='Facturado', default=False)
    estadocita = models.ForeignKey(EstadoCita, on_delete=models.CASCADE, db_column='estadocita_id', verbose_name='Estado de cita', blank=False, null=False)
    totalpago = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='totalpago', verbose_name='Total pago')
    totalpagado = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='totalpagado', verbose_name='Total pagado')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='perfil_id', verbose_name='Perfil')
    recetamedica = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE, db_column='recetamedica_id', verbose_name='Receta médica')

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'Cita'


class DetalleCita(models.Model):
    historial = models.ForeignKey(Historial, on_delete=models.CASCADE, db_column='historial_id', verbose_name='Historial', blank=False, null=False)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita_id', verbose_name='Cita', blank=False, null=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, db_column='servicio_id', verbose_name='Servicio', blank=False, null=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'Detalle de cita'
        verbose_name_plural = 'Detalle de citas'
        db_table = 'DetalleCita'
