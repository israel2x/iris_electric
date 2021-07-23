import pprint
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Suministro
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


class AlimentadorasView(TemplateView):
   template_name = 'administration/alimentadoras.html'


class EmpresasView(TemplateView):
   template_name = 'administration/empresas.html'


class RegionalesView(TemplateView):
   template_name = 'administration/regionales.html'


class SubEstacionesView(TemplateView):
   template_name = 'administration/subestaciones.html'


class TransformadoresView(TemplateView):
   template_name = 'administration/transformadores.html'