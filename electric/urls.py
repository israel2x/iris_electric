from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    # Django config Apps Urls
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Apps
    path('', include('administration.urls', namespace='administration')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)