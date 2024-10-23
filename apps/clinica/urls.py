from django.urls import path
from . import views

urlpatterns = [
    path('lista_citas/', views.ListaCitaTemplateView.as_view(),name='lista-citas'),
    path('lista_servicios/', views.ListaServicioTemplateView.as_view(),name='lista-servicios'),
    path('agregar_servicio/',views.ServicioCreateView.as_view(),name='agregar-servicio'),
    path('agregar_cita/',views.CitaCreateView.as_view(),name='agregar-cita'),
]