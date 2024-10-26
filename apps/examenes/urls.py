from django.urls import path
from . import views

urlpatterns = [
    path('lista_examenes_internos/', views.ListaExamenesInternosTemplateView.as_view(),name='lista-examenes-internos'),
    path('lista_examenes_externos/', views.ListaExamenesExternosTemplateView.as_view(),name='lista-examenes-externos'),
    path('agregar_examen_interno/', views.ExamenInternoCreateView.as_view(),name='agregar-examen-interno'),
    path('editar_examen_interno/<int:pk>/', views.ExamenInternoEditView.as_view(),name='editar-examen-interno'),
    path('agregar_examen_externo/', views.ExamenExternoCreateView.as_view(),name='agregar-examen-externo'),
    path('editar_examen_externo/<int:pk>/', views.ExamenExternoEditView.as_view(),name='editar-examen-externo'),
]