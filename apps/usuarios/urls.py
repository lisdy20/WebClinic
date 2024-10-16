from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsuariosTemplateView.as_view()),
    path('lista', views.UsuariosListTemplateView.as_view(),name='lista-empleados'),
]