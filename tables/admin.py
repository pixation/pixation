from tables.developer import Developer
from tables.api_management import APIManagement
from tables.source import Source
from tables.media import Media
from tables.cached_media import CachedMedia
from django.contrib import admin

admin.site.register(Developer)
admin.site.register(APIManagement)
admin.site.register(Source)
admin.site.register(Media)
admin.site.register(CachedMedia)
