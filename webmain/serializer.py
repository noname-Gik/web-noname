from rest_framework.serializers import ModelSerializer

from webmain.models import ButtonMode, PhotoFile


class ButtonModeSerializer(ModelSerializer):
    class Meta:
        model = ButtonMode
        fields = '__all__'


class PhotoFileSerializer(ModelSerializer):
    class Meta:
        model = PhotoFile
        fields = '__all__'
