from django.db import models
from datetime import datetime
from apps.usuarios.models import Perfil

# Create your models here.
class RecetaMedica(models.Model):
    fecha = models.DateTimeField(default=datetime.now(), db_column='fecha', verbose_name='Fecha de receta', blank=False, null=False)
    doctor = models.ForeignKey(Perfil,on_delete=models.PROTECT,db_column='doctor',verbose_name='Doctor',blank=True,null=True,default=None)
    observaciones = models.TextField(max_length=255, db_column='observaciones', verbose_name='Observaciones', blank=True, null=True)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Receta médica'
        verbose_name_plural = 'Recetas médicas'
        db_table = 'recetamedica'

    def __str__(self) -> str:
        return f'{self.fecha} - {self.observaciones}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class Medicamento(models.Model):
    medicamento = models.CharField(max_length=30, db_column='medicamento', verbose_name='Medicamento', blank=False, null=False)
    descripcion = models.TextField(max_length=255, db_column='descripcion', verbose_name='Descripción', blank=True, null=True)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        db_table = 'medicamentos'

    def __str__(self) -> str:
        return f'{self.medicamento}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class DetalleRecetaMe(models.Model):
    dosiscantidad = models.TextField(max_length=255, db_column='dosiscantidad', verbose_name='Dosis en cantidad', blank=False, null=False)
    dosistiempo = models.TextField(max_length=255, db_column='dosistiempo', verbose_name='Dosis en tiempo', blank=False, null=False)
    recetamedica = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE, db_column='recetamedica', verbose_name='Receta médica', blank=False, null=False)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, db_column='medicamento', verbose_name='Medicamento', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Detalle de receta médica'
        verbose_name_plural = 'Detalles de recetas médicas'
        db_table = 'detallerecetamedica'

    def __str__(self) -> str:
        return f'Medicamento: {self.dosiscantidad} de {self.medicamento} cada {self.dosistiempo}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()
        