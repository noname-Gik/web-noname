from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .api import ButtonModeViewSet, PhotoFileViewSet

router = DefaultRouter()
router.register(r'buttonmode', ButtonModeViewSet),
router.register(r'photofile', PhotoFileViewSet),

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.PhotoFile, name="PhotoFile"),
]
