from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class CustomUser(AbstractUser):


   def toJSON(self):
      item = {}
      item['id'] = self.pk
      item['f_name'] = self.first_name
      item['l_name'] = self.last_name
      item['email'] = self.email
      item['username'] = self.username

      try:
         perfil_name = self.groups.all()[0]
      except:
         perfil_name = 'Sin Perfil Seleccionado'

      if perfil_name == 'Sin Perfil Seleccionado':
         item['perfil'] = perfil_name
      else:
         perfil_name = perfil_name.name
         item['perfil'] = perfil_name
      return item


class Perfiles(Group):
   description = models.CharField(max_length=100)

   def __str__(self):
      return self.name

   def toJSON(self):
      item = {}
      item['id'] = self.id
      item['name'] = self.name
      item['description'] = self.description
      
      return item

