# proyecto/urls.py (el principal, usualmente junto a settings.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),  # Aquí se enlaza el urls.py de la app
]
