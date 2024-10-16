from django.contrib import admin
from .models import TipoAntecedente, Paciente, Antecedente, ContactoPaciente
# Register your models here.

@admin.register(TipoAntecedente)
class TipoAntecedenteAdmin(admin.ModelAdmin):
    list_display=['nombre']

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'dpi', 'nit','direccion']
    search_fields=['nombre', 'apellido', 'dpi', 'nit','direccion']
    list_filter=['genero']

@admin.register(Antecedente)
class AntecedenteAdmin(admin.ModelAdmin):
    list_display=['paciente', 'tipoantecedente']

@admin.register(ContactoPaciente)
class ContactoPacienteAdmin(admin.ModelAdmin):
    list_display=['paciente', 'numcel', 'numcasa', 'contactoemergencia']
    search_fields=['paciente']