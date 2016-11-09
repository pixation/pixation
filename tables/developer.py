from django.contrib.auth.models import User
from django.db import models

class Developer(models.Model):
    user = models.ForeignKey(User)