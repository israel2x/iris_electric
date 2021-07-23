from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib import messages


from .forms import (
   CustomUserCreationForm, CustomUserChangeForm,
   CreatePerfilForm,
)
from .models import Perfiles

User = get_user_model()


class CreateUser(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('administration:usuarios')
   success_message = "Usuario creado exitosamente"
   template_name = 'administration/usuarios/create_user.html'


   def form_valid(self, form):
      group_id = self.request.POST.get('groups')
      group_list = Group.objects.filter(pk=group_id)
      self.object = form.save(commit=False)
      self.object.save()

      self.object.groups.set(group_list)
      self.object.save()
      return super(CreateUser, self).form_valid(form)


class EditUser(LoginRequiredMixin, SuccessMessageMixin, View):
   template_name = 'administration/usuarios/edit_user.html'
   user = None
   
   def dispatch(self, request, pk, *args, **kwargs):
      self.user = User.objects.get(pk=pk)
      return super().dispatch(request, pk, *args, **kwargs)

   def get(self, request, pk):
      form = CustomUserChangeForm(instance=self.user)

      ctx = {
         'form': form,
      }
      return render(request, self.template_name, ctx)
   
   def post(self, request, pk, *args, **kwargs):
      form = CustomUserChangeForm(request.POST, instance=self.user)
      print()
      print(form.is_valid())
      print()
      print(form.cleaned_data)
      print()

      if form.is_valid():
         group_id = self.request.POST.get('groups')
         group_list = Group.objects.filter(pk=group_id)
         self.object = form.save(commit=False)
         self.object.save()

         self.object.groups.set(group_list)
         self.object.save()

         messages.success(request, "Los datos fueron actualizado correctamente")
         return redirect('administration:usuarios')
      messages.warning(request, "Los datos fueron actualizado correctamente")
      return redirect('administration:usuarios')


class CreatePerfilView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   form_class = CreatePerfilForm
   success_url = reverse_lazy('administration:perfiles')
   success_message = "Perfil creado exitosamente"
   template_name = 'administration/perfiles/create_perfil.html'


class EditPerfilView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = Perfiles
   form_class = CreatePerfilForm
   success_url = reverse_lazy('administration:perfiles')
   success_message = "Perfil editado exitosamente"
   template_name = 'administration/perfiles/edit_perfil.html'