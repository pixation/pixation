from tables.developer import Developer
from tables.api_management import APIManagement
from tables.sources import Sources
from tables.media import Media
from django.contrib import admin

admin.site.register(Developer)
admin.site.register(APIManagement)
admin.site.register(Sources)
admin.site.register(Media)
