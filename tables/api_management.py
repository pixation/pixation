from tables.developer import Developer
from django.db import models

class APIManagement(models.Model):
    developer = models.ForeignKey(Developer,on_delete=models.CASCADE)
    key = models.CharField(max_length=64)
    quota = models.BigIntegerField()
