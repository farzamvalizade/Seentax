from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    point = models.PositiveIntegerField(default=0, verbose_name="امتیاز")
    bio = models.CharField(
        max_length=300, blank=True, null=True, verbose_name="توضیحات"
    )
