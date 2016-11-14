from tables.api_management import APIManagement
from django.db import models

class Source(models.Model):
    apimanagement = models.ForeignKey(APIManagement, on_delete=models.CASCADE)
    host = models.CharField(max_length=2000)
    