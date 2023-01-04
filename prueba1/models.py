from django.db import models

# Create your models here.
class project(models.Model):
    nombre = models.CharField(max_length=100)
    