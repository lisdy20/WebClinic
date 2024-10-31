from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers

# Create your views here.
class ListaCitaTemplateView(views.GenericTemplateView):
    template_name = 'lista_citas.html'

    def get(self, request):
        url = reverse('citas-list',request=request)
        url_edit = reverse_lazy('editar-cita',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-cita')
        data = self.get_paginator(request=request,model=models.Cita)
        campos = admin.CitaAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    

class ListaServicioTemplateView(views.GenericTemplateView):
    template_name = 'lista_servicios.html'

    def get(self, request):
        url = reverse('servicios-list',request=request)
        url_edit = reverse_lazy('editar-servicio',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-servicio')
        data = self.get_paginator(request=request,model=models.Servicio)
        campos = admin.ServicioAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    

# - - - - - - - - - - - - - - - - - - - - - -

class ServicioCreateView(views.GenericTemplateView):
    template_name='agregar_servicio.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.ServicioForm
        url = reverse('servicios-list',request=request)
        url_list = reverse_lazy('lista-servicios')
        url_edit = reverse_lazy('editar-servicio',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    

class ServicioEditView(views.GenericTemplateView):
    template_name = 'editar_servicio.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Servicio, pk=kwargs['pk'])
        form = forms.ServicioForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('servicios-list',request=request)
        url_list = reverse_lazy('lista-servicios')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)

class CitaCreateView(views.GenericTemplateView):
    template_name='agregar_cita.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.CitaForm
        url = reverse('citas-list',request=request)
        url_list = reverse_lazy('lista-citas')
        url_edit = reverse_lazy('editar-cita',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    
class CitaEditView(views.GenericTemplateView):
    template_name = 'editar_cita.html'
    
    def get(self, request, *args, **kwargs):
        from apps.pagos.models import ControlPago
        from apps.pagos.forms import ControlPagoForm
        from apps.medicamentos.forms import RecetaMedicaForm,DetalleRecetaForm
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Cita, pk=kwargs['pk'])
        detalles = models.DetalleCita.objects.filter(cita=entity,activo=True)
        pagos = ControlPago.objects.filter(cita=entity,activo=True)
        form = forms.CitaForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('citas-list',request=request)
        url_api_pagos = reverse('pagos-list',request=request)
        url_api_historiales = reverse('historiales-list',request=request)
        url_api_detalles = reverse('detalles-citas-list',request=request)
        url_api_detalles_receta = reverse('detalles-receta-list',request=request)
        url_api_receta = reverse('receta-medica-list',request=request)
        url_list = reverse_lazy('lista-citas')
        url_antecedentes = reverse_lazy('editar-antecedente',kwargs={'pk':0})
        url_antecedentes = str(url_antecedentes).replace('0/','')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['url_antecedentes'] = url_antecedentes
        data['form']=form
        data['entity']=entity
        data['detalles']=detalles
        data['pagos']=pagos
        data['formdetalle']=forms.DetalleCitaForm
        data['formpago']=ControlPagoForm
        data['formhistorial']=forms.HistorialForm
        data['formreceta']=RecetaMedicaForm
        data['formdetallereceta']=DetalleRecetaForm
        data['url_api_detalles_receta']=url_api_detalles_receta
        data['url_api_receta']=url_api_receta
        data['url_api_detalles']=url_api_detalles
        data['url_api_pagos']=url_api_pagos
        data['url_api_historiales']=url_api_historiales
        return render(request=request, template_name=self.template_name,context=data)

# ---------------------------------------------------------------- DRF Views
class ServicioViewSet(views.GenericViewSet):
    queryset = models.Servicio.objects.filter(activo=True)
    serializer_class = serializers.ServicioSerializer

class CitaViewSet(views.GenericViewSet):
    queryset = models.Cita.objects.filter(activo=True)
    serializer_class = serializers.CitaSerializer

class DetalleCitaViewSet(views.GenericViewSet):
    queryset = models.DetalleCita.objects.filter(activo=True)
    serializer_class = serializers.DetalleCitaSerializer

class HistorialViewSet(views.GenericViewSet):
    queryset = models.Historial.objects.filter(activo=True)
    serializer_class = serializers.HistorialSerializer