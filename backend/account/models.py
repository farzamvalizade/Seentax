from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    point = models.PositiveIntegerField(default=0, verbose_name="امتیاز")
