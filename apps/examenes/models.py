from django.db import models
from apps.clinica.models import Cita
from apps.clinica.models import DetalleCita

# Create your models here.

class ExLaboratorio(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita', verbose_name='Cita', blank=False, null=False)
    motivo = models.CharField(max_length=80, db_column='motivo', verbose_name='Motivo del examen', blank=False, null=False)
    nombrelab = models.CharField(max_length=80, db_column='nombrelab', verbose_name='Nombre del laboratorio', blank=True, null=True)

    class Meta:
        verbose_name = 'Examen de laboratorio'
        verbose_name_plural = 'Exámenes de laboratorio'
        db_table = 'ExLaboratorio'

class DocResLaboratorio(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre del documento', blank=False, null=False)
    ubicacion = models.FileField(db_column='ubicacion', verbose_name='Ubicación', blank=False, null=False)
    exlaboratorio = models.ForeignKey(ExLaboratorio, on_delete=models.CASCADE, db_column='exlaboratorio_id', verbose_name='Examen de laboratorio', blank=False, null=False)

    class Meta:
        verbose_name = 'Documento de resultado de examen laboratorio'
        verbose_name_plural = 'Documentos de resultados de exámenes laboratorio'
        db_table = 'DocResLaboratorio'

class ExInterno(models.Model):
    detallecita = models.ForeignKey(DetalleCita, on_delete=models.CASCADE, db_column='detallecita', verbose_name='Cita', blank=False, null=False)
    motivo = models.CharField(max_length=80, db_column='motivo', verbose_name='Motivo del examen', blank=False, null=False)
    nombredoctor = models.CharField(max_length=80, db_column='nombredoc', verbose_name='Doctor que realiza examen', blank=True, null=True)

    class Meta:
        verbose_name = 'Examen interno'
        verbose_name_plural = 'Exámenes internos'
        db_table = 'ExInterno'

class DocResInterno(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre del documento', blank=False, null=False)
    ubicacion = models.FileField(db_column='ubicacion', verbose_name='Ubicación', blank=False, null=False)
    exinterno = models.ForeignKey(ExInterno, on_delete=models.CASCADE, db_column='exinterno_id', verbose_name='Examen interno', blank=False, null=False)

    class Meta:
        verbose_name = 'Documento de resultado de examen interno'
        verbose_name_plural = 'Documentos de resultados de exámenes internos'
        db_table = 'DocResInterno'

