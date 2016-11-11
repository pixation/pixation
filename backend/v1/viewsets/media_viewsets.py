from rest_framework import viewsets, filters
from backend.v1.serializers.media_serializer import MediaUploadSerializer
from tables.media import Media

class MediaUploadViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaUploadSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)