from rest_framework.viewsets import ModelViewSet

from webcomment.models import СommentMode
from webcomment.serializer import СommentModeSerializer


class СommentModeViewSet(ModelViewSet):
    queryset = СommentMode.objects.all()
    serializer_class = СommentModeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
