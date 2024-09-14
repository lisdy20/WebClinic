from django.contrib import admin
from .models import TipoPago, ControlPago

# Register your models here.
@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
    list_display=['nombre']

@admin.register(ControlPago)
class ControlPagoAdmin(admin.ModelAdmin):
    list_display=['cita', 'tipopago']