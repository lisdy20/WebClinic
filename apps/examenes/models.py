from django.db import models
from apps.clinica.models import Cita,DetalleCita
from apps.usuarios.models import Perfil

# Create your models here.

class ExLaboratorio(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, db_column='cita', verbose_name='Cita', blank=False, null=False)
    motivo = models.CharField(max_length=80, db_column='motivo', verbose_name='Motivo del examen', blank=False, null=False)
    nombrelab = models.CharField(max_length=80, db_column='nombrelab', verbose_name='Nombre del laboratorio', blank=True, null=True)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Examen de laboratorio'
        verbose_name_plural = 'Exámenes de laboratorio'
        db_table = 'ExLaboratorio'

    def __str__(self):
        return f'Examen en {self.nombrelab} por {self.motivo}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class DocResLaboratorio(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre del documento', blank=False, null=False)
    ubicacion = models.FileField(db_column='ubicacion', verbose_name='Ubicación', blank=False, null=False)
    exlaboratorio = models.ForeignKey(ExLaboratorio, on_delete=models.CASCADE, db_column='exlaboratorio_id', verbose_name='Examen de laboratorio', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Documento de resultado de examen laboratorio'
        verbose_name_plural = 'Documentos de resultados de exámenes laboratorio'
        db_table = 'DocResLaboratorio'
    
    def __str__(self):
        return f'{self.nombre}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class ExInterno(models.Model):
    detallecita = models.ForeignKey(DetalleCita, on_delete=models.CASCADE, db_column='detallecita', verbose_name='Cita', blank=False, null=False)
    motivo = models.CharField(max_length=80, db_column='motivo', verbose_name='Motivo del examen', blank=False, null=False)
    nombredoctor = models.CharField(max_length=80, db_column='nombredoc', verbose_name='Doctor que realiza examen', blank=True, null=True)
    doctor = models.ForeignKey(Perfil,verbose_name='Encargado', on_delete=models.CASCADE,db_column='doctor_encargado',blank=True,null=True,default=None)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Examen interno'
        verbose_name_plural = 'Exámenes internos'
        db_table = 'ExInterno'

    def __str__(self):
        return f'Examen realizado por {self.motivo} hecho por {self.nombredoctor}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

class DocResInterno(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre del documento', blank=False, null=False)
    ubicacion = models.FileField(db_column='ubicacion', verbose_name='Ubicación', blank=False, null=False)
    exinterno = models.ForeignKey(ExInterno, on_delete=models.CASCADE, db_column='exinterno_id', verbose_name='Examen interno', blank=False, null=False)
    activo = models.BooleanField(default=True, db_column='activo',verbose_name='Activo')

    class Meta:
        verbose_name = 'Documento de resultado de examen interno'
        verbose_name_plural = 'Documentos de resultados de exámenes internos'
        db_table = 'DocResInterno'

    def __str__(self):
        return f'{self.nombre}'
    
    def detele(self,**kwargs):
        self.activo = False
        self.save()

