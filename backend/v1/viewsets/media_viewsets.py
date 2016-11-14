from django.http import *
from django.contrib.auth.models import User

from rest_framework import viewsets, filters
from rest_framework.response import Response

from backend.v1.serializers.media_serializer import *
from tables.media import Media


class MediaUploadViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    http_method_names = ['post'] 
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    

class MediaPublicFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    http_method_names = ['get']
    
    def list(self, request):        
        queryset = Media.objects.filter(public=1)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = MediaSerializer(
            page, 
            many=True,
            context={'request': request}
            )
            return self.get_paginated_response(serializer.data)
        
        serializer = MediaSerializer(
            queryset, 
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)
      

class MediaUserFeedViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    http_method_names = ['get']
    def list(self, request):
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Media.objects.filter(owner=user)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = MediaSerializer(
                    page, 
                    many=True,
                    context={'request': request}
                    )
                return self.get_paginated_response(serializer.data)
            
            serializer = MediaSerializer(
                    queryset, 
                    many=True,
                    context={'request': request}
                    )
            return Response(serializer.data)
        
        else:
            return HttpResponse(status=401)
    