from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webcontainer.api import OrganizationTableModeViewSet, RoleTableModeViewSet, UserTableModeViewSet, \
    ConnectionTableModeViewSet
from webmain.api import ButtonModeViewSet, PhotoFileViewSet, AdviceModeViewSet, TicketModeViewSet

router = DefaultRouter()
# Регистры разных компонентов
router.register(r'buttonmode', ButtonModeViewSet),
router.register(r'advicemode', AdviceModeViewSet),
router.register(r'ticketmode', TicketModeViewSet),
router.register(r'photofile', PhotoFileViewSet),
# Регистр данных в database
router.register(r'organizations', OrganizationTableModeViewSet),
router.register(r'roles', RoleTableModeViewSet),
router.register(r'users', UserTableModeViewSet),
router.register(r'connections', ConnectionTableModeViewSet),

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('webmain.urls')),
                  path('api/', include(router.urls)),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
