from django.conf.urls import url, include
from rest_framework import routers
from backend.v1.viewsets.media_viewsets import MediaViewSet

router = routers.DefaultRouter()
router.register('images', MediaViewSet, 'v1/images')
urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
print(router.urls)