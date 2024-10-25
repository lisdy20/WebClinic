from django.urls import path
from . import views

urlpatterns = [
    path('lista_examenes_internos/', views.ListaExamenesInternosTemplateView.as_view(),name='lista-examenes-internos'),
    path('lista_examenes_externos/', views.ListaExamenesExternosTemplateView.as_view(),name='lista-examenes-externos'),
    path('agregar_examen_interno/', views.ExamenInternoCreateView.as_view(),name='agregar-examen-interno'),
    path('editar_examenes_interno/<int:pk>/', views.ExamenInternoEditView.as_view(),name='editar-examen-interno'),
]