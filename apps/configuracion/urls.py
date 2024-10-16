from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.ServiciosTemplateView.as_view(),name='servicios'),
    path('nuestro_equipo/', views.NuestroEquipoTemplateView.as_view(),name='equipo'),
    path('contacto/', views.ContactoTemplateView.as_view(),name='contacto'),
    path('dashboard/', views.PanelTemplateView.as_view(),name='panel'),
]