from django.conf.urls import url, include

from backend.v1.routers.media_router import *
from backend.v1.routers.developer_router import *
from backend.v1.views.image_resize import *

urlpatterns = [
    url(r'^images/', include(media_router.urls)),
    url(r'^developer/',include(developer_router.urls)),
    url(r'^resize', image_resize)
]