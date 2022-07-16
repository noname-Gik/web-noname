from rest_framework.serializers import ModelSerializer

from webmessage.models import FileMessageMode


class FileMessageModeSerializer(ModelSerializer):
    class Meta:
        model = FileMessageMode
        fields = '__all__'
