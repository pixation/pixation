from rest_framework import routers

from backend.v1.viewsets.developer_viewsets import *

developer_router = routers.DefaultRouter()
developer_router.register(
    'makeDeveloper',
    MakeDeveloperViewSet,
    'v1 Developer Set'
)