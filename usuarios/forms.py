from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

   groups = forms.ModelChoiceField(
      queryset=Group.objects.all(),
      widget=forms.Select(attrs={'class': 'form-control'})
   )

   class Meta(UserCreationForm):
      model = CustomUser
      fields = ('username', 'email', 'first_name', 'last_name', 'groups')


class CustomUserChangeForm(UserChangeForm):

   groups = forms.ModelChoiceField(
      queryset=Group.objects.all(),
      widget=forms.Select(attrs={'class': 'form-control'})
   )

   class Meta:
      model = CustomUser
      fields = ('username', 'email', 'first_name', 'last_name', 'groups')