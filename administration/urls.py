from django.urls import path

from .views import (
   IndexView, UsuariosView,
   SuministroView,
)



app_name = 'administration'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('administration/usuario/', UsuariosView.as_view(), name='usuarios'),
   path('administration/suministro/', SuministroView.as_view(), name='suministro'),

]