from django.db import models

# Create your models here.

class TipoAntecedente(models.Model):
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre', blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de antecedente'
        verbose_name_plural = 'Tipo de antecedentes'
        db_table = 'TipoAntecedente'


class Paciente(models.Model):
    GENEROS_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    nombre = models.CharField(max_length=30, db_column='nombre', verbose_name='Nombre', blank=True, null=True)
    apellido = models.CharField(max_length=30, db_column='apellido', verbose_name='Apellido', blank=True, null=True)
    dpi = models.CharField(max_length=14, db_column='dpi', verbose_name='DPI', blank=True, null=True)
    nit = models.CharField(max_length=10, db_column='nit', verbose_name='NIT', blank=True, null=True)
    direccion = models.CharField(max_length=30, db_column='direccion', verbose_name='Dirección', blank=True, null=True)
    fechanac = models.DateField(db_column='fechanac', verbose_name='Fecha de nacimiento', blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENEROS_CHOICES, db_column='genero', verbose_name='Género', blank=True, null=True)
    telefono = models.CharField(max_length=15, db_column='telefono', verbose_name='Teléfono', blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'pacientes'

class Antecedente(models.Model):
    tipoantecedente = models.ForeignKey(TipoAntecedente, on_delete=models.CASCADE, db_column='tipoantecedente', verbose_name='Tipo de antecedente', blank=False, null=False)
    descripcion = models.TextField(max_length=255, db_column='descripcion', verbose_name='Descripción', blank=False, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente', verbose_name='Paciente', blank=False, null=False)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'
        db_table = 'antecedentes'

class ContactoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente_id', verbose_name='Paciente', blank=False, null=False)
    numcel = models.CharField(max_length=15, db_column='numcel', verbose_name='Número de celular', blank=True, null=True)
    numcasa = models.CharField(max_length=15, db_column='numcasa', verbose_name='Número de casa', blank=True, null=True)
    contactoemergencia = models.BooleanField(default=False, db_column='contactoemergencia', verbose_name='Contacto de emergencia')

    class Meta:
        verbose_name = 'Contacto de paciente'
        verbose_name_plural = 'Contactos de pacientes'
        db_table = 'contactopaciente'
        