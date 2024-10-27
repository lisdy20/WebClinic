from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsuariosTemplateView.as_view()),
    path('lista_empleados', views.UsuariosListTemplateView.as_view(),name='lista-empleados'),
    path('agregar_empleado', views.EmpleadoCreateView.as_view(),name='agregar-empleados'),
    path('editar_empleado', views.EmpleadoEditView.as_view(),name='editar-empleados'),
]