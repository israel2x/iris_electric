from django.urls import path

from .views import (
   IndexView, UsuariosView,
   SuministroView, PerfilesView,
)



app_name = 'administration'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('administration/usuario/', UsuariosView.as_view(), name='usuarios'),
   path('administration/perfiles/', PerfilesView.as_view(), name='perfiles'),
   path('administration/suministro/', SuministroView.as_view(), name='suministro'),
   
]