from django.contrib import admin

from .models import *

admin.site.register(Empresa)
admin.site.register(Regional)
admin.site.register(SubEstacion)
admin.site.register(Alimentadora)
admin.site.register(Transformador)
admin.site.register(Suministro)
admin.site.register(Medidor)
admin.site.register(RegistroMedidor)
