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
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
            'owner',
        )
        read_only_fields = fields
        extra_kwargs={'owner_name':''}    

class MediaUserFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
        )
        read_only_fields = fields