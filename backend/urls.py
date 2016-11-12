from django.conf.urls import url, include 

from rest_framework import routers


urlpatterns = [
    url(r'^v1/', include('backend.v1.urls', namespace='v1')),
    url(r'^v2/', include('backend.v2.urls', namespace='v2')),
]