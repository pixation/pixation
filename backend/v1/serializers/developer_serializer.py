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

    def create(self, validated_data):
        sources_data = validated_data.pop('sources')
        api_management = APIManagement.objects.create(**validated_data)
        for source_data in sources_data:
        # print(sources_data)
            Source.objects.create(api_management=api_management, **sources_data)
        return api_management

class DeveloperSerializer(serializers.ModelSerializer):
    # api_management = APIManagementSerializer(many=True)
    developer_name = serializers.StringRelatedField(
        many=False,
        source='user.username',    
    )
    class Meta:
        model = Developer
        fields = (
            'developer_name',
            # 'api_management'
        )