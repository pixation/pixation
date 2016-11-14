from rest_framework import routers

from backend.v1.viewsets.media_viewsets import *

media_router = routers.DefaultRouter()
media_router.register(
    'upload', 
    MediaUploadViewSet, 
    'v1 Upload Image'
    )
media_router.register(
    'getPublicFeed', 
    MediaPublicFeedViewSet, 
    'v1 Public Feed'
    )
media_router.register(
    'getUserFeed', 
    MediaUserFeedViewSet, 
    'v1 User Feed'
    )
