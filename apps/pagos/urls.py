from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.PagosListTemplateView.as_view(),name='lista-pagos')
]