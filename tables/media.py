from django.db import models
from django.contrib.auth.models import User
import uuid

def create_unique_filename(instance, filename):
    extension = filename.split(".")[-1]
    instance.old_filename = filename
    instance.filename = "{}.{}".format(uuid.uuid4(),extension)
    return instance.filename

class Media(models.Model):
    display_name = models.CharField(max_length=64)
    filename = models.CharField(max_length=64)
    old_filename = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=create_unique_filename,width_field=width, height_field=height)
