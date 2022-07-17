from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webcontainer.api import OrganizationTableModeViewSet, RoleTableModeViewSet, UserTableModeViewSet, \
    ConnectionTableModeViewSet
from webcontainer.views import get_organization, get_roles, get_users, get_roles_all
from webmain.api import ButtonModeViewSet, PhotoFileViewSet, AdviceModeViewSet, TicketModeViewSet
from webmain.models import PhotoFile
from webmain.views import home, advice_home
from webmessage.api import FileMessageModeViewSet
from webmessage.views import FileMessageList

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
# Регистр работы с данными
router.register(r'filemessages', FileMessageModeViewSet),

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  # соединение с стр. home, advice_zone
                  path('', home, name='home'),
                  path('advice_zone/', advice_home, name='advice_home'),
                  # отображение файлов на сайте
                  path('', PhotoFile, name="PhotoFile"),
                  # вывод данных через api
                  path('advice_zone/api/get_organization', get_organization),
                  path('advice_zone/api/get_roles_all', get_roles_all),
                  path('advice_zone/api/get_roles/<int:ids>', get_roles),
                  path('advice_zone/api/get_users', get_users),
                  # отправка сообщений с файлом
                  path('api/filemessages/', FileMessageList.as_view(), name="send_message_form"),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
