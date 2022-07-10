from rest_framework.serializers import ModelSerializer

from webcontainer.models import OrganizationTableMode, RoleTableMode, UserTableMode, ConnectionTableMode


class OrganizationTableModeSerializer(ModelSerializer):
    class Meta:
        model = OrganizationTableMode
        fields = '__all__'


class RoleTableModeSerializer(ModelSerializer):
    class Meta:
        model = RoleTableMode
        fields = '__all__'


class UserTableModeSerializer(ModelSerializer):
    class Meta:
        model = UserTableMode
        fields = '__all__'


class ConnectionTableModeSerializer(ModelSerializer):
    class Meta:
        model = ConnectionTableMode
        fields = '__all__'
