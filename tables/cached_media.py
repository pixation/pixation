from django.db import models
from django.contrib.auth.models import User
from tables.media import Media

class CachedMedia(Media):
    # TODO: Add array entry for api type of object removal
    original = models.ForeignKey(Media, 
        related_name='original_image',
        on_delete=models.CASCADE
        )
    api_type = models.CharField(max_length=1)
    last_hit_at = models.DateTimeField(auto_now_add=True)
