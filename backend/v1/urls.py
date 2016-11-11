from django.conf.urls import url, include
from rest_framework import routers
from backend.v1.viewsets.media_viewsets import MediaUploadViewSet

router = routers.DefaultRouter()
router.register('images/upload', MediaUploadViewSet)
urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
print(router.urls)