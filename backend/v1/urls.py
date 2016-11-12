from django.conf.urls import url, include
from rest_framework import routers
from backend.v1.viewsets.media_viewsets import *

router = routers.DefaultRouter()

router.register(
    'images/upload', 
    MediaUploadViewSet, 
    'images/upload'
    )

router.register(
    'images/getPublicFeed', 
    MediaPublicFeedViewSet, 
    'images/getPublicFeed'
    )

router.register(
    'images/getUserFeed', 
    MediaUserFeedViewSet, 
    'images/getUserFeed'
    )

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]