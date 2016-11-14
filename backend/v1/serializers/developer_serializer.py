from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from tables.developer import Developer
from tables.api_management import APIManagement
from tables.source import Source
class DeveloperSerializer(serializers.ModelSerializer):
    developer_name = serializers.StringRelatedField(
        many=False,
        source='user.username',    
    )
    class Meta:
        model = Developer
        fields = (
            'developer_name',
        )

class APIManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIManagement
        fields = (
        )

class SourceSerializer(serializers.ModelSerializer):
    api_management = APIManagementSerializer(many=True)

    class Meta:
        model = Source
        fields = (
            'hosts',
        )