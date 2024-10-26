from django.urls import path
from . import views

urlpatterns = [
    path('lista_pacientes/', views.ListaPacientesTemplateView.as_view(),name='lista-pacientes'),
    path('agregar_paciente/', views.PacienteCreateView.as_view(),name='agregar-paciente'),
    path('editar_paciente/<int:pk>/', views.PacienteEditView.as_view(),name='editar-paciente'),
]