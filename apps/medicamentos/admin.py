from django.contrib import admin
from .models import RecetaMedica, Medicamento, DetalleRecetaMe

# Register your models here.

class DetalleRecetaInLine(admin.TabularInline):
    model=DetalleRecetaMe

@admin.register(RecetaMedica)
class RecetaMedicaAdmin(admin.ModelAdmin):
    inlines= [DetalleRecetaInLine]
    list_display=['fecha', 'observaciones']
    list_filter=['activo']

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display=['medicamento', 'descripcion']
    search_fields=['medicamento']
    list_filter=['activo']

@admin.register(DetalleRecetaMe)
class DetalleRecetaMeAdmin(admin.ModelAdmin):
    list_display=['recetamedica', 'medicamento', 'dosiscantidad', 'dosistiempo']
    search_fields=['recetamedica']
    list_filter=['activo']