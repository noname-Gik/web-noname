from rest_framework.viewsets import ModelViewSet

from webmessage.models import FileMessageMode
from webmessage.serializer import FileMessageModeSerializer


class FileMessageModeViewSet(ModelViewSet):
    queryset = FileMessageMode.objects.all()
    serializer_class = FileMessageModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']



