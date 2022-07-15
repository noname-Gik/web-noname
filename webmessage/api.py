from rest_framework.viewsets import ModelViewSet

from webmessage.models import MessageMode, PhotoFileMode
from webmessage.serializer import MessageModeSerializer, PhotoFileModeSerializer


class MessageModeViewSet(ModelViewSet):
    queryset = MessageMode.objects.all()
    serializer_class = MessageModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class PhotoFileModeViewSet(ModelViewSet):
    queryset = PhotoFileMode.objects.all()
    serializer_class = PhotoFileModeSerializer
    http_method_names = ['get', 'post', 'options']
