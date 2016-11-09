from tables.api_management import APIManagement
from django.db import models

class Sources(models.Model):
    apimanagement = models.ForeignKey(APIManagement, on_delete=models.CASCADE)
