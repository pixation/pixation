from tables.api_management import APIManagement
from django.db import models

class Source(models.Model):
    api_management = models.ForeignKey(
        APIManagement, 
        related_name='sources',
        on_delete=models.CASCADE)
    host = models.CharField(
        max_length=2000,
        null=True
        )
    