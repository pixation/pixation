from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from rest_framework import serializers

from tables.media import Media


class MediaSerializer(serializers.ModelSerializer):
    link = serializers.ReadOnlyField(source='get_link')
    owner_name = serializers.StringRelatedField(
        many=False,
        source='owner.username',
        read_only=True
        )
    class Meta:
        model = Media
        fields = (
            'image',
            'link',
            'display_name',
            'owner_name',
            'public',
        )



