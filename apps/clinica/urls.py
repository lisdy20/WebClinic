from django.urls import path
from . import views

urlpatterns = [
    path('lista_citas/', views.ListaCitaTemplateView.as_view(),name='lista_citas'),
]