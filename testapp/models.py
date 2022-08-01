from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=20)
