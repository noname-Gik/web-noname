from rest_framework.serializers import ModelSerializer

from webmessage.models import MessageMode, PhotoFileMode


class MessageModeSerializer(ModelSerializer):
    class Meta:
        model = MessageMode
        fields = '__all__'


class PhotoFileModeSerializer(ModelSerializer):
    class Meta:
        model = PhotoFileMode
        fields = '__all__'
