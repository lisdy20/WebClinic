from django.contrib import admin
from .models import EstadoCita, Historial, Servicio, Cita, DetalleCita

# Register your models here.

class DetalleCitaInLine(admin.TabularInline):
    model=DetalleCita

@admin.register(EstadoCita)
class EstadoCitaAdmin(admin.ModelAdmin):
    list_display=['NombreEstado']


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display=['motivo', 'historiaenfer', 'diagnostico']
    search_fields=['motivo','historiaenfer','diagnostico']
    list_filter=['activo']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display=['nombreservicio', 'descripcion', 'costo']
    search_fields=['nombreservicio']
    list_filter=['activo']

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    inlines=[DetalleCitaInLine]
    list_display=['fecha', 'paciente', 'numaut', 'numserie', 'dte', 'facturado', 'estado', 'totalpago','diferencia_pago', 'totalpagado','pagado']
    search_fields=['paciente', 'numaut', 'numserie', 'dte']
    list_filter=['activo']

@admin.register(DetalleCita)
class DetalleCitaAdmin(admin.ModelAdmin):
    list_display=['historial', 'cita', 'servicio', 'subtotal']
    list_filter=['activo']