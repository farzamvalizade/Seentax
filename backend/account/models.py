from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class User(AbstractUser):
    point = models.PositiveIntegerField(default=0, verbose_name="امتیاز")
    bio = models.CharField(
        max_length=300, blank=True, null=True, verbose_name="توضیحات"
    )


class PointLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="point_logs")
    old_point = models.IntegerField()
    new_point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.old_point} -> {self.new_point}"


@receiver(pre_save, sender=User)
def create_point_log(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return
    if old_user.point != instance.point:
        PointLog.objects.create(
            user=instance,
            old_point=old_user.point,
            new_point=instance.point,
        )
