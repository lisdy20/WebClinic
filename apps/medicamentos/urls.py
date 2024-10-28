from django.urls import path
from . import views

urlpatterns = [
    path('lista_medicamentos/', views.ListaMedicamentoTemplateView.as_view(),name='lista-medicamentos'),
    path('agregar_medicamento/', views.MedicamentoCreateView.as_view(),name='agregar-medicamento'),
    path('editar_medicamento/<int:pk>/', views.MedicamentoEditView.as_view(),name='editar-medicamento'),
    path('editar_receta/<int:pk>/', views.RecetaMedicaEditView.as_view(),name='editar-receta'),
]