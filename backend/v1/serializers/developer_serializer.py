from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from tables.developer import Developer

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
