from rest_framework import viewsets, filters
from backend.v1.serializers.media_serializer import MediaSerializer
from tables.media import Media
from rest_framework.response import Response
from django.http import *

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def list(self, request):
        if self.request.user.is_authenticated:
            if "n" in self.request.query_params:
                queryset = Media.objects.filter(owner=self.request.user)[:int(self.request.query_params["n"][0])]
            else:
                queryset = Media.objects.filter(owner=self.request.user)[:10]
            serializer = MediaSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse(status=401)
        

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)