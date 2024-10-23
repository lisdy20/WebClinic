from django.urls import path
from . import views

urlpatterns = [
    path('lista_citas/', views.ListaMedicamentoTemplateView.as_view(),name='lista-medicamento'),
    path('agregar_citas/', views.MedicamentoCreateView.as_view(),name='agregar-medicamento'),
]