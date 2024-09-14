from django.db import models
from apps.clinica.models import Cita

# Create your models here.

class TipoPago(models.Model): 
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre tipo de pago', blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de pago'
        verbose_name_plural = 'Tipos de pagos'
        db_table = 'TipoPago'

class ControlPago(models.Model):
    cantidadpago = models.DecimalField(max_digits=10,decimal_places=2, db_column='cantidadpago', verbose_name='Cantidad de pago', blank=False, null=False)
    descripcion = models.TextField(max_length=255, db_column='descripcion', verbose_name='Descripción', blank=True, null=True)
    tipopago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, db_column='tipopago', verbose_name='Tipo de pago', blank=False, null=False)
    numref = models.CharField(max_length=30, db_column='numref', verbose_name='Número de referencia', blank=True, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita', verbose_name='Cita', blank=False, null=False)

    class Meta:
        verbose_name = 'Control de pago'
        verbose_name_plural = 'Control de pagos'
        db_table = 'ControlPago'
        