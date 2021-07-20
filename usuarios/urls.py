from django.urls import path


from .views import LoginView


app_name = 'usuarios'

urlpatterns = [
   path('login/', LoginView.as_view(), name='login'),
]