from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Perfiles

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

   groups = forms.ModelChoiceField(
      queryset=Group.objects.all(),
      widget=forms.Select(attrs={'class': 'form-control'})
   )

   class Meta(UserCreationForm):
      model = User
      fields = ('username', 'email', 'first_name', 'last_name', 'groups')


class CustomUserChangeForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   groups = forms.ModelChoiceField(
      queryset=Group.objects.all(),
   )

   username = forms.CharField(widget=forms.TextInput())
   email = forms.EmailField(widget=forms.EmailInput())
   first_name = forms.CharField(widget=forms.TextInput())
   last_name = forms.CharField(widget=forms.TextInput())

   class Meta:
      model = User
      fields = ['username', 'email', 'first_name', 'last_name', 'groups']


class CreatePerfilForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for form in self.visible_fields():
         form.field.widget.attrs['class'] = 'form-control'

   
   class Meta:
      model = Perfiles
      fields = ('name', 'description', 'permissions')