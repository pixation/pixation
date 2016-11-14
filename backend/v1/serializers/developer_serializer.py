from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from tables.developer import Developer
from tables.api_management import APIManagement
from tables.source import Source

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'hosts',
        )

class APIManagementSerializer(serializers.ModelSerializer):
    sources = SourceSerializer(many=True)
    developer_name = serializers.StringRelatedField(
        many=False,
        source='developer.user.username',    
    )
    class Meta:
        model = APIManagement
        fields = (
            'developer_name',
            'key',
            'quota',
            'sources'
        )

class DeveloperSerializer(serializers.ModelSerializer):
    api_management = APIManagementSerializer(many=True)
    developer_name = serializers.StringRelatedField(
        many=False,
        source='user.username',    
    )
    class Meta:
        model = Developer
        fields = (
            'developer_name',
            'api_management'
        )