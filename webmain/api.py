from rest_framework.viewsets import ModelViewSet

from webmain.models import ButtonMode, PhotoFile, AdviceMode, TicketMode
from webmain.serializer import ButtonModeSerializer, PhotoFileSerializer, AdviceModeSerializer, TicketModeSerializer


class ButtonModeViewSet(ModelViewSet):
    queryset = ButtonMode.objects.all()
    serializer_class = ButtonModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class AdviceModeViewSet(ModelViewSet):
    queryset = AdviceMode.objects.all()
    serializer_class = AdviceModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class TicketModeViewSet(ModelViewSet):
    queryset = TicketMode.objects.all()
    serializer_class = TicketModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class PhotoFileViewSet(ModelViewSet):
    queryset = PhotoFile.objects.all()
    serializer_class = PhotoFileSerializer
    http_method_names = ['get', 'post', 'options']
