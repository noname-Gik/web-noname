from rest_framework.serializers import ModelSerializer

from webmain.models import ButtonMode, PhotoFile, AdviceMode, TicketMode


class ButtonModeSerializer(ModelSerializer):
    class Meta:
        model = ButtonMode
        fields = '__all__'


class AdviceModeSerializer(ModelSerializer):
    class Meta:
        model = AdviceMode
        fields = '__all__'

class TicketModeSerializer(ModelSerializer):
    class Meta:
        model = TicketMode
        fields = '__all__'

class PhotoFileSerializer(ModelSerializer):
    class Meta:
        model = PhotoFile
        fields = '__all__'
