import pprint
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model

from .models import Suministro

User = get_user_model()



class IndexView(TemplateView):
   template_name = 'administration/index.html'


class PerfilesView(TemplateView):
   template_name = 'administration/perfiles.html'

class AlimentadorasView(TemplateView):
   template_name = 'administration/alimentadoras.html'

class EmpresasView(TemplateView):
   template_name = 'administration/empresas.html'

class RegionalesView(TemplateView):
   template_name = 'administration/regionales.html'

class SubEstacionesView(TemplateView):
   template_name = 'administration/subestaciones.html'


class UsuariosView(TemplateView):
   template_name = 'base/usuarios_list_base.html'

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
         else:
            data['error'] = 'Ha ocurrido un error'
      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)


class SuministroView(TemplateView):
   template_name = 'base/suministro_list_base.html'


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


# class SuministroView(View):
# 	template_name = 'Subasta/list/list.html'
# 	user = None
	
	
# 	@method_decorator(csrf_exempt)
# 	def dispatch(self, request, *args, **kwargs):
# 		self.user = self.request.user
# 		return super().dispatch(request, *args, **kwargs)

# 	def get(self, request, *args, **kwargs):

# 		if self.user.userprofile.proveedor.nombre == 'Comprador': # If its comprador
# 			context = {
# 				'comprador': True,
# 				'title': 'Procesos de Subastas',
# 			}
# 			# return render(self.request, self.template_name, context)
# 		elif self.user.userprofile.proveedor.nombre == 'Proveedor':
# 			context = {
# 				'title': 'Procesos de Subastas',
# 			}
# 		return render(self.request, self.template_name, context)
			
# 	def post(self, request, *args, **kwargs):
# 		data = {}
# 		provider_status_permision = (
# 			'P', 'S', 'TS', 
# 			'TF', 'F',
# 		)
# 		try:
# 			action = request.POST['action']
# 			if action == 'searchdata':
# 				data = []
# 				if self.user.userprofile.proveedor.nombre == 'Comprador': # if comprador
# 					for i in Subasta.objects.filter(created_by=self.user):
# 						i.update_status()
# 						data.append(i.toJSON())
# 				elif self.user.userprofile.proveedor.nombre == 'Proveedor': #if proveedor
# 					for i in Subasta.objects.filter(providers=self.user, status__in=provider_status_permision):
# 						i.update_status()
# 						data.append(i.toJSON())
# 			else:
# 				data['error'] = 'Ha ocurrido un error'
# 		except Exception as e:
# 			data['error'] = str(e)
# 		return JsonResponse(data, safe=False)



class TransformadoresView(TemplateView):
   template_name = 'administration/transformadores.html'