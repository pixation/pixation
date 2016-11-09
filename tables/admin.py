from tables.developer import Developer
from tables.api_management import APIManagement
from tables.media import Media
from django.contrib import admin

admin.site.register(Developer)
admin.site.register(APIManagement)
admin.site.register(Media)
