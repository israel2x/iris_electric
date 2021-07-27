from django.urls import path

from .views import (
   IndexView, UsuariosView, PerfilesView,
   SuministroView, SuministroCreateView, SuministroUpdateView,
   EmpresasView, EmpresaCreateView, EmpresaUpdateView,
   RegionalesView, RegionalCreateView, RegionalUpdateView,
   SubEstacionesView, SubEstacionCreateView, SubEstacionUpdateView,
   AlimentadorasView, AlimentadoraCreateView, AlimentadoraUpdateView,
   TransformadoresView, TransformadorCreateView, TransformadorUpdateView,
   MedidorListView, MedidorDetailView, MedidorCreateView, MedidorUpdateView,
)


app_name = 'administration'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('administration/usuario/', UsuariosView.as_view(), name='usuarios'),
   path('administration/perfiles/', PerfilesView.as_view(), name='perfiles'),
   # Empresas URL's
   path('administration/empresas/', EmpresasView.as_view(), name='empresas'),
   path('empresa/create-empresa/', EmpresaCreateView.as_view(), name='create_empresa'),
   path('empresa/edit-empresa/<int:pk>/', EmpresaUpdateView.as_view(), name='edit_empresa'),
   # Regionales URL's
   path('administration/regionales/', RegionalesView.as_view(), name='regionales'),
   path('regionales/create-regional/', RegionalCreateView.as_view(), name='create_regional'),
   path('regionales/edit-regional/<int:pk>/', RegionalUpdateView.as_view(), name='edit_regional'),
   # SubEstacion URL's
   path('administration/subestacion/', SubEstacionesView.as_view(), name='subestacion'),
   path('subestacion/create-subestacion/', SubEstacionCreateView.as_view(), name='create_subestacion'),
   path('subestacion/edit-subestacion/<int:pk>/', SubEstacionUpdateView.as_view(), name='edit_subestacion'),
   # Alimentadora URL's
   path('administration/alimentadora/', AlimentadorasView.as_view(), name='alimentadora'),
   path('alimentadora/create-alimentadora/', AlimentadoraCreateView.as_view(), name='create_alimentadora'),
   path('alimentadora/edit-alimentadora/<int:pk>/', AlimentadoraUpdateView.as_view(), name='edit_alimentadora'),
   # Transformador URL's
   path('administration/transformador/', TransformadoresView.as_view(), name='transformador'),
   path('transformador/create-transformador/', TransformadorCreateView.as_view(), name='create_transformador'),
   path('transformador/edit-transformador/<int:pk>/', TransformadorUpdateView.as_view(), name='edit_transformador'),
   # Suministro URL's
   path('administration/suministro/', SuministroView.as_view(), name='suministro'),
   path('create-suministro/', SuministroCreateView.as_view(), name='create_suministro'),
   path('edit-suministro/<int:pk>/', SuministroUpdateView.as_view(), name='edit_suministro'),
   # Medidor URL's
   path('administration/suministro/medidor/<int:pk>/', MedidorListView.as_view(), name='list_medidor'),
   path('administration/suministro/medidor/<int:pk>/detail/', MedidorDetailView.as_view(), name='detail_medidor'),
   path('<int:pk>/create/', MedidorCreateView.as_view(), name='create_medidor'),
   path('administration/suministro/medidor/<int:pk>/edit/', MedidorUpdateView.as_view(), name='edit_medidor'),
   
]