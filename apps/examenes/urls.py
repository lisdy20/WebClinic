from django.urls import path
from . import views

urlpatterns = [
    path('lista_examenes_internos/', views.ListaExamenesInternosTemplateView.as_view(),name='lista-examenes-internos'),
    path('lista_examenes_externos/', views.ListaExamenesExternosTemplateView.as_view(),name='lista-examenes-externos'),
]