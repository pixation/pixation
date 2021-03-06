from django.conf.urls import url, include

from backend.v1.routers.media_router import *
from backend.v1.routers.developer_router import *
from backend.v1.views.image_resize import *
from backend.v1.views.image_resize_developer import *
from backend.v1.views.api_management import *
urlpatterns = [
    url(r'^images/', include(media_router.urls)),
    url(r'^developer/',include(developer_router.urls)),
    url(r'^resize/', image_resize),
    url(r'^smartresize/',image_resize2),
    url(r'^remove/',image_remove),
    url(r'^refreshkey/',refresh_key),
    url(r'^deletekey/',delete_key),
]