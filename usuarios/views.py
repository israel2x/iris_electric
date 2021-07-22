from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm
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


# class EditUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#    form_class = CustomUserChangeForm
#    success_url = reverse_lazy('administration:usuarios')
#    success_message = "Usuario creado exitosamente"
#    template_name = 'administration/usuarios/edit_user.html'


#    def form_valid(self, form):
#       group_id = self.request.POST.get('groups')
#       group_list = Group.objects.filter(pk=group_id)
#       self.object = form.save(commit=False)
#       self.object.save()

#       self.object.groups.set(group_list)
#       self.object.save()
#       return super(EditUser, self).form_valid(form)


class EditUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = User
   form_class = CustomUserChangeForm
   success_url = reverse_lazy('administration:usuarios')
   success_message = "Usuario creado exitosamente"
   template_name = 'administration/usuarios/edit_user.html'


   def form_valid(self, form):
      group_id = self.request.POST.get('groups')
      group_list = Group.objects.filter(pk=group_id)
      self.object = form.save(commit=False)
      self.object.save()

      self.object.groups.set(group_list)
      self.object.save()
      return super(EditUser, self).form_valid(form)