from django.urls import path
from . import views

urlpatterns = [
    path('lista_pacientes/', views.ListaPacientesTemplateView.as_view(),name='lista_pacientes'),
]