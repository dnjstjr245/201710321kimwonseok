from django.db import models

# Create your models here.

class Members(models.Model):
    username = models.CharField(max_length=30, verbose_name="name")
    password = models.CharField(max_length=30, verbose_name="pass")
