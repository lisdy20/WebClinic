from django.db import models
from datetime import datetime
from decimal import Decimal
from django.db.models import Sum
from rest_framework.exceptions import APIException

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

    def __str__(self):
        return f'{self.NombreEstado}'

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
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'
        db_table = 'Historial'

    def __str__(self):
        return f'Historial de {self.paciente} por {self.motivo}'
    
    def save(self,**kwargs):
        if self.activo == False:
            raise APIException('Una vez eliminado no se puede modificar.')
        return super().save(**kwargs)
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class Servicio(models.Model):
    nombreservicio = models.CharField(max_length=30, db_column='nombreservicio', verbose_name='Nombre del servicio', blank=False, null=False)
    descripcion = models.CharField(max_length=80, db_column='descripcion', verbose_name='Descripción del servicio', blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, db_column='costo', verbose_name='Costo del servicio', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'Servicio'

    def __str__(self):
        return f'{self.nombreservicio}: Q{self.costo}'
    
    def save(self,**kwargs):
        if self.activo == False:
            raise APIException('Una vez eliminado no se puede modificar.')
        return super().save(**kwargs)
        
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class Cita(models.Model):
    EN_ESPERA='EE'
    EN_CONSULTA='EC'
    FINALIZADA='F'
    CANCELADA='C'
    ESTADO_CHOICES=[
        (EN_ESPERA, 'En espera'),
        (EN_CONSULTA, 'En consulta'),
        (FINALIZADA, 'Finalizada'),
        (CANCELADA, 'Cancelada'),
    ]
    fecha = models.DateTimeField(default=datetime.now(), db_column='fecha', verbose_name='Fecha de cita', blank=False, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente_id', verbose_name='Paciente', blank=True, null=False)
    numaut = models.CharField(max_length=80, db_column='numaut', verbose_name='Número de autorización', blank=True, null=True,default=None)
    numserie = models.CharField(max_length=80, db_column='numserie', verbose_name='Número de serie', blank=True, null=True,default=None)
    dte = models.CharField(max_length=80, db_column='dte', verbose_name='DTE', blank=True, null=True,default=None)
    facturado = models.BooleanField(db_column='facturado', verbose_name='Facturado', default=False)
    estado = models.CharField(max_length=2, db_column='estado',verbose_name='Estado', blank=False, null=False,default=EN_ESPERA,choices=ESTADO_CHOICES)
    estadocita = models.ForeignKey(EstadoCita, on_delete=models.CASCADE, db_column='estadocita_id', verbose_name='Estado de cita', blank=True, null=True,default=None)
    totalpago = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='totalpago', verbose_name='Total pago')
    totalpagado = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='totalpagado', verbose_name='Total pagado')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='perfil_id', verbose_name='Perfil',blank=True)
    recetamedica = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE, db_column='recetamedica_id', verbose_name='Receta médica',null=True,blank=True,default=None)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'Cita'

    def __str__(self) -> str:
        return f'Cita #{self.id} hecha el {self.fecha} para {self.paciente}'
    
    def save(self,**kwargs):
        self.facturado = True if self.numaut and self.numserie and self.dte else False
        if self.activo == 0:
            raise APIException('Una vez eliminado no se puede modificar.')
        return super().save(**kwargs)
    
    def pagado(self):
        return self.totalpagado==self.totalpago and self.totalpago != 0
    
    @property
    def pago_pendiente(self):
        return self.totalpago - self.totalpagado
    
    def actualizar_total_pagado(self):
        # Sumar todos los pagos activos y actualizar el campo totalpagado
        self.totalpagado = self.totalpagado_excluyendo()
        self.save(update_fields=['totalpagado'])

    def totalpagado_excluyendo(self, pago_id=None):
        from apps.pagos.models import ControlPago
        # Calcula el total pagado excluyendo el pago con ID pago_id (útil para evitar duplicados en actualización)
        pagos = ControlPago.objects.filter(cita=self, activo=True)
        if pago_id:
            pagos = pagos.exclude(id=pago_id)
        return pagos.aggregate(total=Sum('cantidadpago'))['total'] or Decimal(0)
    
    def calcular_total_detalle(self):
        # Sumar subtotales de detalles activos de la cita
        total = DetalleCita.objects.filter(cita=self, activo=True).aggregate(total=Sum('subtotal'))['total']
        return total or Decimal(0)
    
    def actualizar_total_pago(self):
        # Actualizar el campo totalpago con la suma de subtotales activos
        self.totalpago = self.calcular_total_detalle()
        self.save(update_fields=['totalpago'])
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()


class DetalleCita(models.Model):
    historial = models.ForeignKey(Historial, on_delete=models.CASCADE, db_column='historial_id', verbose_name='Historial', blank=True, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita_id', verbose_name='Cita', blank=False, null=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, db_column='servicio_id', verbose_name='Servicio', blank=False, null=False)
    descuento = models.DecimalField(verbose_name='Descuento',max_digits=10,decimal_places=2,default=0)
    subtotal = models.DecimalField(verbose_name='Subtotal',max_digits=10, decimal_places=2,default=0, blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Detalle de cita'
        verbose_name_plural = 'Detalle de citas'
        db_table = 'DetalleCita'

    def __str__(self):
        return f'{self.servicio.nombreservicio} por {self.servicio.costo}'
    
    def save(self,**kwargs):
        if self.activo == False:
            raise Exception('Una vez eliminado no se puede modificar.')
        if self.descuento<=self.servicio.costo:
            if self.cita.FINALIZADA == self.cita.estado or self.cita.CANCELADA == self.cita.estado:
                raise Exception('La cita debe estar en espera o en consulta.')
            if not self.activo:
                raise Exception('El registro ya está eliminado no puede agregar más detalles.')
            self.subtotal = self.servicio.costo - self.descuento
            super().save(**kwargs)
            self.cita.actualizar_total_pago()
        else:
            raise Exception('El descuento no puede ser mayor al costo.')
        
    def detele(self,**kwargs):
        self.cita.actualizar_total_pago()
        self.activo = False
        self.save()
    
