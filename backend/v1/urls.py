from django.conf.urls import url, include

from rest_framework import routers

from backend.v1.viewsets.media_viewsets import *
from backend.v1.viewsets.developer_viewsets import *


images_router = routers.DefaultRouter()
images_router.register(
    'upload', 
    MediaUploadViewSet, 
    'v1 Upload Image'
    )
images_router.register(
    'getPublicFeed', 
    MediaPublicFeedViewSet, 
    'v1 Public Feed'
    )
images_router.register(
    'getUserFeed', 
    MediaUserFeedViewSet, 
    'v1 User Feed'
    )


developer_router = routers.DefaultRouter()
developer_router.register(
    'makeDeveloper',
    DeveloperViewSet,
    'v1 Developer Set'
)

urlpatterns = [
    url(r'^images/', include(images_router.urls)),
    url(r'^developer/',include(developer_router.urls)),
]