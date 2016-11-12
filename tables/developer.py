from django.contrib.auth.models import User
from django.db import models

class Developer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username