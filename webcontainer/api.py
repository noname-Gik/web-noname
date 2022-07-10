from rest_framework.viewsets import ModelViewSet

from webcontainer.models import OrganizationTableMode, RoleTableMode, UserTableMode, ConnectionTableMode
from webcontainer.serializer import OrganizationTableModeSerializer, RoleTableModeSerializer, UserTableModeSerializer, \
    ConnectionTableModeSerializer


# API - модели
class OrganizationTableModeViewSet(ModelViewSet):
    queryset = OrganizationTableMode.objects.all()
    serializer_class = OrganizationTableModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class RoleTableModeViewSet(ModelViewSet):
    queryset = RoleTableMode.objects.all()
    serializer_class = RoleTableModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class UserTableModeViewSet(ModelViewSet):
    queryset = UserTableMode.objects.all()
    serializer_class = UserTableModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class ConnectionTableModeViewSet(ModelViewSet):
    queryset = ConnectionTableMode.objects.all()
    serializer_class = ConnectionTableModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
