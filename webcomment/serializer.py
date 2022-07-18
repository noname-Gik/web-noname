from rest_framework.serializers import ModelSerializer

from webcomment.models import СommentMode


class СommentModeSerializer(ModelSerializer):
    class Meta:
        model = СommentMode
        fields = '__all__'
