from django.urls import path


from .views import CreateUser, EditUser


app_name = 'usuarios'

urlpatterns = [
   path('create-user/', CreateUser.as_view(), name='create_user'),
   path('edit-user/<int:pk>/', EditUser.as_view(), name='edit_user'),

]