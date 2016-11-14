from tables.developer import Developer
from django.db import models

class APIManagement(models.Model):
    developer = models.ForeignKey(
        Developer, 
        related_name='api_management',
        on_delete=models.CASCADE
        )
    key = models.CharField(max_length=64)
    quota = models.BigIntegerField()

    def __str__(self):
        return "{} - {} - {}".format(
            self.pk,
            self.developer.user.username,
            self.quota
            )