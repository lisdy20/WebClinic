from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.PagosListTemplateView.as_view(),name='lista-pagos'),
    path('agregar_pago/', views.PagosCreateView.as_view(),name='agregar-pago'),
    path('editar_pago/<int:pk>/', views.PagoEditView.as_view(),name='editar-pago'),
]