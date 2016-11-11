from rest_framework import serializers
from tables.media import Media

class MediaUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'pk',
            'image',
            'display_name',
        )