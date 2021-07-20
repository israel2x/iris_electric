from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
   
   def toJSON(self):
      item = model_to_dict(self)
      item['f_name'] = self.first_name
      item['l_name'] = self.last_name
      item['email'] = self.email
      item['username'] = self.username

      return item
