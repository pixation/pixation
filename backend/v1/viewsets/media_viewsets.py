from rest_framework import viewsets, filters
from backend.v1.serializers.media_serializer import *
from tables.media import Media
from rest_framework.response import Response
from django.http import *

class MediaUploadViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaUploadSerializer
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
class MediaPublicFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaPublicFeedSerializer
    def list(self, request):
        if "n" in self.request.query_params:
            queryset = Media.objects.filter(public=1)[:int(self.request.query_params["n"][0])]
        else:
            queryset = Media.objects.filter(public=1)[:10]
        serializer = MediaPublicFeedSerializer(queryset, many=True)
        return Response(serializer.data)
        
class MediaUserFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaUserFeedSerializer
    def list(self, request):
        if self.request.user.is_authenticated:
            if "n" in self.request.query_params:
                queryset = Media.objects.filter(owner=self.request.user)[:int(self.request.query_params["n"][0])]
            else:
                queryset = Media.objects.filter(owner=self.request.user)[:10]
            serializer = MediaUserFeedSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse(status=401)
    