from django.conf.urls import url, include

from rest_framework import routers

from backend.v1.viewsets.media_viewsets import *


images_router = routers.DefaultRouter()
images_router.register(
    'upload', 
    MediaUploadViewSet, 
    'images/upload'
    )
images_router.register(
    'getPublicFeed', 
    MediaPublicFeedViewSet, 
    'images/getPublicFeed'
    )
images_router.register(
    'getUserFeed', 
    MediaUserFeedViewSet, 
    'images/getUserFeed'
    )

urlpatterns = [
    url(r'^v1/images/', include(images_router.urls)),
]