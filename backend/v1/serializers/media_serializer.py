from django.contrib.auth.models import User

from rest_framework import serializers

from tables.media import Media

class MediaUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
            'public',
        )
        
class MediaPublicFeedSerializer(serializers.ModelSerializer):
    owner_name = serializers.StringRelatedField(
        many=False,
        source='owner.username',
        read_only=True
        )
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
            'owner_name',
        )

class MediaUserFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
        )