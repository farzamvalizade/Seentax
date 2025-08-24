from django.db import models

from account.models import User

# Create your models here.


class Category(models.Model):
    programming_language = models.CharField(
        max_length=100, verbose_name="زبان برنامه‌نویسی"
    )
    field = models.CharField(max_length=100, verbose_name="شاخه")


class Problem(models.Model):

    LEVELS_CHOICE = [("easy", "آسان"), ("medium", "متسوط"), ("hard", "سخت")]

    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    category = models.ForeignKey(
        Category, verbose_name="دسته بندی", on_delete=models.CASCADE
    )
    level = models.CharField(max=10, choices=LEVELS_CHOICE, verbose_name="سطح")
    point = models.PositiveIntegerField(default=10, verbose_name="امتیاز")


class Solve(models.Model):
    user = models.ForeignKey(User, verbose_name="حل شده توسط", on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, verbose_name="سوال", on_delete=models.CASCADE)
    solved_at = models.DateTimeField(auto_now_add=True, verbose_name="حل شده در تاریخ")
