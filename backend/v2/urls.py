from django.conf.urls import url, include

from rest_framework import routers

from backend.v2.viewsets.media_viewsets import *


router = routers.DefaultRouter()
router.register(
    'upload', 
    MediaUploadViewSet, 
    'v2 Upload Image'
    )
router.register(
    'getPublicFeed', 
    MediaPublicFeedViewSet, 
    'v2 Public Feed'
    )
router.register(
    'getUserFeed', 
    MediaUserFeedViewSet, 
    'v2 User Feed'
    )

urlpatterns = [
    url(r'^images/', include(router.urls)),
]