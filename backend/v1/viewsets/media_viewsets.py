from django.http import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import Http404

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

class MediaResizeViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaResizeSerializer
    http_method_names = ['post'] 
    
    def perform_create(self, serializer):
        request = self.request
        width = request.POST['width']
        height = request.POST['height']
        img =  request.POST['image']
        ext = img.split('.')[-1]
        if request.user.is_authenticated:
            username = request.user.username
            query = (Media.objects.filter(owner__username=username).filter(image=img) | Media.objects.filter(public=True)).first()
            if query is not None:
                imgpath = os.path.join(settings.MEDIA_ROOT,img)
                image = Image.open(imgpath)
                image = image.resize((width, height), PIL.Image.ANTIALIAS)
                filename = uuid.uuid4() + '.' + ext
                image.save(os.path.join(settings.MEDIA_ROOT,filename))
                reopen = open(os.path.join(settings.MEDIA_ROOT,filename),'r')
                django_file = File(reopen)
                serializer.save(
                    display_name = query.display_name + ' Resized',
                    public = True,
                    image = filename,
                    owner = self.request.user
                    )
            else:
                raise Http404
        else:
            return redirect('/login?next=/upload')

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
    
