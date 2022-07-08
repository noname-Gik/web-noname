from rest_framework.viewsets import ModelViewSet

from webmain.models import ButtonMode, PhotoFile
from webmain.serializer import ButtonModeSerializer, PhotoFileSerializer


class ButtonModeViewSet(ModelViewSet):
    queryset = ButtonMode.objects.all()
    serializer_class = ButtonModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class PhotoFileViewSet(ModelViewSet):
    queryset = PhotoFile.objects.all()
    serializer_class = PhotoFileSerializer
    http_method_names = ['get', 'post', 'options']
