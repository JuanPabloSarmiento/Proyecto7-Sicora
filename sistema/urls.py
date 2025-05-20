# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sistema.views import ZonaRiegoViewSet

router = DefaultRouter()
router.register(r'zonas', ZonaRiegoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]