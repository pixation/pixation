from rest_framework import viewsets, filters
from backend.v1.serializers.media_serializer import MediaSerializer
from tables.media import Media

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)