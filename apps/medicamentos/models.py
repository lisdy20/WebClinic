from django.db import models
from datetime import datetime

# Create your models here.
class RecetaMedica(models.Model):
    fecha = models.DateTimeField(default=datetime.now(), db_column='fecha', verbose_name='Fecha de receta', blank=False, null=False)
    observaciones = models.TextField(max_length=255, db_column='observaciones', verbose_name='Observaciones', blank=False, null=False)

    class Meta:
        verbose_name = 'Receta médica'
        verbose_name_plural = 'Recetas médicas'
        db_table = 'recetamedica'

class Medicamento(models.Model):
    medicamento = models.CharField(max_length=30, db_column='medicamento', verbose_name='Medicamento', blank=False, null=False)
    descripcion = models.TextField(max_length=255, db_column='descripcion', verbose_name='Descripción', blank=True, null=True)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        db_table = 'medicamentos'

class DetalleRecetaMe(models.Model):
    dosiscantidad = models.TextField(max_length=255, db_column='dosiscantidad', verbose_name='Dosis en cantidad', blank=False, null=False)
    dosistiempo = models.TextField(max_length=255, db_column='dosistiempo', verbose_name='Dosis en tiempo', blank=False, null=False)
    recetamedica = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE, db_column='recetamedica', verbose_name='Receta médica', blank=False, null=False)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, db_column='medicamento', verbose_name='Medicamento', blank=False, null=False)

    class Meta:
        verbose_name = 'Detalle de receta médica'
        verbose_name_plural = 'Detalles de recetas médicas'
        db_table = 'detallerecetamedica'
        