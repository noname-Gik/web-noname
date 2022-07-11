from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webcontainer.api import OrganizationTableModeViewSet, RoleTableModeViewSet, UserTableModeViewSet, \
    ConnectionTableModeViewSet
from webcontainer.views import get_organization, get_roles, get_users
from webmain.api import ButtonModeViewSet, PhotoFileViewSet, AdviceModeViewSet, TicketModeViewSet
from webmain.models import PhotoFile
from webmain.views import home, advice_home

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
                  path('api/', include(router.urls)),
                  # соединение с стр. home, advice_zone
                  path('', home, name='home'),
                  path('advice_zone/', advice_home, name='advice_home'),
                  # отображение файлов на сайте
                  path('', PhotoFile, name="PhotoFile"),
                  # вывод данных через api
                  path('api/get_organization', get_organization),
                  path('api/get_roles', get_roles),
                  path('api/get_users', get_users),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
