from django.contrib import admin
from .models import TipoPago, ControlPago

# Register your models here.
@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
    list_display=['nombre']
    search_fields=['nombre']
    list_filter=['activo']

@admin.register(ControlPago)
class ControlPagoAdmin(admin.ModelAdmin):
    list_display=['id','cantidadpago','cita', 'tipopago','descripcion','numref']
    search_fields=['descripcion','numref']
    list_filter=['activo']