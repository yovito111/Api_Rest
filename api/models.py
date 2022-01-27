from msilib.schema import Class
from unicodedata import name
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    fundations = models.PositiveBigIntegerField()
