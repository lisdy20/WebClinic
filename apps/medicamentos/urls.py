from django.urls import path
from . import views

urlpatterns = [
    path('lista_medicamentos/', views.ListaMedicamentoTemplateView.as_view(),name='lista-medicamento'),
    path('agregar_medicamento/', views.MedicamentoCreateView.as_view(),name='agregar-medicamento'),
]