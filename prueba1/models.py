from django.db import models

# Create your models here.
class project(models.model):
    nombre = models.CharField(max_length=100)
    