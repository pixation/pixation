from django.db import models
from django.contrib.auth.models import User
import uuid

def create_unique_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(),extension)

class Media(models.Model):
    image = models.ImageField(
        upload_to=create_unique_filename,
        width_field='width',
        height_field='height'
    )
    display_name = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(self.pk,self.display_name) 