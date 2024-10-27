from django.db import models
from decimal import Decimal
from apps.clinica.models import Cita

# Create your models here.

class TipoPago(models.Model): 
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre tipo de pago', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')
    

    class Meta:
        verbose_name = 'Tipo de pago'
        verbose_name_plural = 'Tipos de pagos'
        db_table = 'TipoPago'

    def __str__(self):
        return f'{self.nombre}'
    
    def save(self,**kwargs):
        if self.activo == False:
            raise Exception('Una vez eliminado no se puede modificar.')
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class ControlPago(models.Model):
    cantidadpago = models.DecimalField(max_digits=10,decimal_places=2, db_column='cantidadpago', verbose_name='Cantidad de pago', blank=False, null=False)
    descripcion = models.TextField(max_length=255, db_column='descripcion', verbose_name='Descripción', blank=True, null=True)
    tipopago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, db_column='tipopago', verbose_name='Tipo de pago', blank=False, null=False)
    numref = models.CharField(max_length=30, db_column='numref', verbose_name='Número de referencia', blank=True, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita', verbose_name='Cita', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Control de pago'
        verbose_name_plural = 'Control de pagos'
        db_table = 'ControlPago'
        
    def __str__(self):
        return f'Se ha pagado {self.cantidadpago} en la cita #{self.cita.id}'
    
    
    def save(self,**kwargs):
        if self.activo == False:
            raise Exception('Una vez eliminado no se puede modificar.')
        
        self.pagar(**kwargs)
        super().save(**kwargs)
    
    def delete(self,**kwargs):
        self.activo = False
        self.save()
        self.descontar()
    

    def pagar(self):
        # Excluye el pago actual si es una actualización para calcular el pago pendiente
        pago_actual = ControlPago.objects.filter(id=self.id).first()
        pago_anterior = pago_actual.cantidadpago if pago_actual else Decimal(0)

        # Calcular el pago pendiente de la cita sin considerar el pago actual (si está en edición)
        pago_pendiente = self.cita.pago_pendiente + pago_anterior

        if self.cantidadpago > pago_pendiente:
            raise Exception("Pago excede el monto pendiente de la cita.")

        # Guardar y actualizar el total pagado en la cita
        super().save()
        self.cita.actualizar_total_pagado()

    def descontar(self):
        if self.cita.totalpagado < self.cantidadpago:
            raise Exception('No se puede descontar más dinero de la cita.')
        self.cita.actualizar_total_pagado()
        
