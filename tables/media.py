from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    server = models.CharField(max_length=64)
    path = models.CharField(max_length=64)
    filename = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    width = models.IntegerField()
    height = models.IntegerField()
