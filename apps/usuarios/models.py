from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TipoPerfil(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre', blank=True, null=True)
    descripcion = models.TextField(db_column='descripcion', verbose_name='Descripción', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Tipo de perfil'
        verbose_name_plural = 'Tipo de perfiles'
        db_table = 'tipo_perfiles'

    def __str__(self):
        return f'{self.nombre} {self.descripcion}'

class Perfil(AbstractUser):
    GENEROS_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE, db_column='tipo_perfil_id', verbose_name='Tipo de perfil', blank=True, null=True)
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre', blank=True, null=True)
    apellido = models.CharField(max_length=30, db_column='apellido', verbose_name='Apellido', blank=True, null=True)
    colegiado = models.IntegerField(db_column='colegiado', verbose_name='Colegiado', blank=True, null=True)
    direccion = models.CharField(max_length=30, db_column='direccion', verbose_name='Dirección', blank=True, null=True)
    fechanac = models.DateField(db_column='fechanac', verbose_name='Fecha de nacimiento', blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENEROS_CHOICES, db_column='genero', verbose_name='Género', blank=True, null=True)
    telefono = models.CharField(max_length=15, db_column='telefono', verbose_name='Teléfono', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        db_table = 'perfiles'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'