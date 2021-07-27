import json
import pprint
import random
from django.shortcuts import render
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, View
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .forms import *
from .models import *
from usuarios.models import Perfiles


User = get_user_model()



class IndexView(LoginRequiredMixin, TemplateView):
   login_url = 'accounts/login/'
   template_name = 'administration/index.html'


class UsuariosView(LoginRequiredMixin, TemplateView):
   template_name = 'base/listas/usuarios/usuarios_list_base.html'
   login_url = 'accounts/login/'


   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_usuarios':
            data = []
            for i in User.objects.all():
               data.append(i.toJSON())
            # print(data)
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class SuministroView(LoginRequiredMixin, TemplateView):
   template_name = 'base/listas/suministros/suministro_list_base.html'
   login_url = 'accounts/login/'


   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_suministros':
            data = []
            for i in Suministro.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class SuministroCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = SuministroForm
   success_url = reverse_lazy('administration:suministro')
   success_message = "Suministro creado exitosamente"
   template_name = 'administration/suministro/create_suministro.html'


class SuministroUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Suministro
   form_class = SuministroForm
   success_url = reverse_lazy('administration:suministro')
   success_message = "Suministro editado exitosamente"
   template_name = 'administration/suministro/edit_suministro.html'


class PerfilesView(TemplateView):
   template_name = 'base/listas/perfiles/perfiles_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_perfiles':
            data = []
            for i in Perfiles.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class EmpresasView(TemplateView):
   template_name = 'base/listas/empresas/empresas_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_empresas':
            data = []
            for i in Empresa.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class EmpresaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = EmpresaCreationForm
   success_url = reverse_lazy('administration:empresas')
   success_message = "Empresa creada exitosamente"
   template_name = 'administration/empresas/create_empresa.html'


class EmpresaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Empresa
   form_class = EmpresaCreationForm
   success_url = reverse_lazy('administration:empresas')
   success_message = "Empresa editada exitosamente"
   template_name = 'administration/empresas/edit_empresa.html'


class RegionalesView(TemplateView):
   template_name = 'base/listas/regionales/regionales_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_regionales':
            data = []
            for i in Regional.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class RegionalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = RegionalForm
   success_url = reverse_lazy('administration:regionales')
   success_message = "Regional creada exitosamente"
   template_name = 'administration/regionales/create_regionales.html'


class RegionalUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Regional
   form_class = RegionalForm
   success_url = reverse_lazy('administration:regionales')
   success_message = "Regional editada exitosamente"
   template_name = 'administration/regionales/edit_regionales.html'


class SubEstacionesView(TemplateView):
   template_name = 'base/listas/subestacion/subestacion_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_subestacion':
            data = []
            for i in SubEstacion.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)

class SubEstacionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = SubEstacionForm
   success_url = reverse_lazy('administration:subestacion')
   success_message = "SubEstacion creada exitosamente"
   template_name = 'administration/subestacion/create_subestacion.html'


class SubEstacionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = SubEstacion
   form_class = SubEstacionForm
   success_url = reverse_lazy('administration:subestacion')
   success_message = "SubEstacion editada exitosamente"
   template_name = 'administration/subestacion/edit_subestacion.html'


class AlimentadorasView(TemplateView):
   template_name = 'base/listas/alimentadora/alimentadora_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_alimentadoras':
            data = []
            for i in Alimentadora.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class AlimentadoraCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = AlimentadoraForm
   success_url = reverse_lazy('administration:alimentadora')
   success_message = "Alimentadora creada exitosamente"
   template_name = 'administration/alimentadora/create_alimentadora.html'


class AlimentadoraUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Alimentadora
   form_class = AlimentadoraForm
   success_url = reverse_lazy('administration:alimentadora')
   success_message = "Alimentadora editada exitosamente"
   template_name = 'administration/alimentadora/edit_alimentadora.html'



class TransformadoresView(TemplateView):
   template_name = 'base/listas/transformador/transformador_list_base.html'

   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_transformador':
            data = []
            for i in Transformador.objects.all():
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class TransformadorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = TransformadorForm
   success_url = reverse_lazy('administration:transformador')
   success_message = "Alimentadora creada exitosamente"
   template_name = 'administration/transformador/create_transformador.html'


class TransformadorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Transformador
   form_class = TransformadorForm
   success_url = reverse_lazy('administration:transformador')
   success_message = "Alimentadora editada exitosamente"
   template_name = 'administration/transformador/edit_transformador.html'


class MedidorListView(TemplateView):
   template_name = 'base/listas/medidor/medidor_list_base.html'
   pk = None

   @method_decorator(csrf_exempt)
   def dispatch(self, request, pk, *args, **kwargs):
      self.pk = pk
      return super().dispatch(request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
      data = {}
      
      try:
         action = request.POST['action']
         if action == 'search_medidor':
            data = []
            for i in Medidor.objects.filter(suministro_id=self.pk):
               data.append(i.toJSON())
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class MedidorDetailView(LoginRequiredMixin, SuccessMessageMixin, View):
   template_name = 'administration/medidor/detail.html'
   pk = None
   obj = None

   @method_decorator(csrf_exempt)
   def dispatch(self, request, pk, *args, **kwargs):
      self.pk = pk
      self.obj = Medidor.objects.filter(suministro_id=self.pk)[0]
      return super().dispatch(request, *args, **kwargs)

   def get(self, *args, **kwargs):
      medidor = self.obj
      eventos = RegistroMedidor.objects.filter(medidor_id=medidor.id)

      context = {
         'medidor': medidor,
         'eventos': eventos,
      }
      return render(self.request, self.template_name, context)
   
   def post(self, *args, **kwargs):
      data = {}
      medidor = self.obj
      res = json.loads(self.request.body)


      try:
         eventos = RegistroMedidor.objects.filter(medidor_id=medidor.id)

         ctx = {
            'eventos': eventos,
         }
         data['html_lista_eventos'] = render_to_string('administration/medidor/tabla_eventos.html', ctx)

         if res['event'] == 'solicitud_lectura':
            new_event = RegistroMedidor()
            new_event.medidor = self.obj
            new_event.origen = 1
            new_event.kwh = round(random.uniform(1000.00, 9999.00), 2)
            new_event.operador = 'TEST'
            new_event.error = 1
            new_event.observacion = 'Solicitud de lectura por parte del sistema.'
         elif res['event'] == 'solicitar_corte':
            new_event = RegistroMedidor()
            new_event.medidor = self.obj
            new_event.origen = 1
            new_event.kwh = round(random.uniform(1000.00, 9999.00), 2)
            new_event.operador = 'TEST'
            new_event.error = 1
            new_event.observacion = 'Solicitud de corte por parte del sistema.'
         else:
            new_event = RegistroMedidor()
            new_event.medidor = self.obj
            new_event.origen = 1
            new_event.kwh = round(random.uniform(1000.00, 9999.00), 2)
            new_event.operador = 'TEST'
            new_event.error = 1
            new_event.observacion = 'Solicitud de reconexion por parte del sistema.'

         new_event.save()
         data['status'] = '200'
         data['message'] = 'Solicitud generada exitosamente'
      except Exception as e:
         data['status'] = '500'
         data['error'] = str(e)
      return JsonResponse(data, safe=False)



class MedidorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = MedidorForm
   success_url = reverse_lazy('administration:suministro')
   success_message = "Medidor creado exitosamente"
   template_name = 'administration/medidor/create_medidor.html'


class MedidorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Medidor
   form_class = MedidorForm
   success_url = reverse_lazy('administration:suministro')
   success_message = "Medidor editado exitosamente"
   template_name = 'administration/medidor/edit_medidor.html'