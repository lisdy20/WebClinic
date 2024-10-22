from django.contrib import admin
from .models import ExLaboratorio, DocResLaboratorio, ExInterno, DocResInterno

# Register your models here.

@admin.register(ExLaboratorio)
class ExLaboratorioAdmin(admin.ModelAdmin):
    list_display=['cita', 'motivo', 'nombrelab']
    search_fields=['cita']

@admin.register(DocResLaboratorio)
class DocResLaboratorioAdmin(admin.ModelAdmin):
    list_display=['nombre', 'exlaboratorio']
    search_fields=['nombre']

@admin.register(ExInterno)
class ExInternoAdmin(admin.ModelAdmin):
    list_display=['detallecita','nombredoctor', 'motivo']
    list_filter=['nombredoctor']

@admin.register(DocResInterno)
class DocResInternoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'exinterno']
    search_fields=['nombre']