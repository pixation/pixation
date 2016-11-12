from django.http import *
from django.contrib.auth.models import User

from rest_framework import viewsets, filters
from rest_framework.response import Response

from backend.v1.serializers.media_serializer import *
from tables.media import Media


class MediaUploadViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaUploadSerializer
    http_method_names = ['post',] 
    print(queryset[0].image)
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    

class MediaPublicFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaPublicFeedSerializer
    http_method_names = ['get']
    
    def list(self, request):
        query_params = self.request.query_params
        if 'n' in query_params:
            n = int(query_params['n'][0])
        else:
            n = 10
        queryset = Media.objects.filter(public=1)[:n]
        serializer = MediaPublicFeedSerializer(
            queryset, 
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)
      

class MediaUserFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaUserFeedSerializer
    http_method_names = ['get']

    def list(self, request):
        if self.request.user.is_authenticated:
            query_params = self.request.query_params
            if 'n' in query_params:
                n = int(query_params['n'][0])
            else:
                n = 10
            user = self.request.user
            queryset = Media.objects.filter(owner=user)[:n]
            serializer = MediaUserFeedSerializer(
                queryset, 
                many=True,
                context={'request': request}
                )
            return Response(serializer.data)
        else:
            return HttpResponse(status=401)
    