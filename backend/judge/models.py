import os

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


def dockerfile_upload_path(instance, filename):

    lang_name = instance.name.replace(" ", "_").lower()
    return os.path.join(f"{lang_name}_dockerfile", filename)


class VerdictChoices(models.TextChoices):
    accepted = ("AC", "Accepted")
    wrong_answer = ("WA", "Wrong Answer")
    time_limit_exceeded = ("TLE", "Time Limit Exceeded")
    memory_limit_exceeded = ("MLE", "Memory Limit Exceeded")
    runtime_error = ("RE", "Runtime Error")
    compile_error = ("CE", "Compile Error")


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=128, verbose_name="نام")
    dockerfile_path = models.FileField(
        upload_to=dockerfile_upload_path, verbose_name="مسیر فایل داکر"
    )
    run_command = models.CharField(max_length=256, verbose_name="دستور اجرا")
    compile_command = models.CharField(
        max_length=256, blank=True, default="", verbose_name="دستور کامپایل"
    )
    need_compile = models.BooleanField(default=False, verbose_name="به کامپایل نیاز دارد؟")
    extension = models.CharField(
        max_length=128, blank=True, default="", verbose_name="پسوند"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "زبان برنامه نویسی"
        verbose_name_plural = "زبان‌های برنامه نویسی"

    def __str__(self):
        return self.name


class Problem(models.Model):
    class DifficultyChoices(models.TextChoices):
        easy = ("Easy", "Easy")
        normal = ("Normal", "Normal")
        hard = ("Hard", "Hard")

    name = models.CharField(max_length=128, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    difficulty = models.CharField(
        max_length=16, choices=DifficultyChoices.choices, verbose_name="درجه سختی"
    )
    languages = models.ManyToManyField(
        ProgrammingLanguage, verbose_name="زبان‌های برنامه نویسی"
    )
    input_format = models.TextField(
        max_length=128, blank=True, default="", verbose_name="فرمت ورودی"
    )
    output_format = models.TextField(max_length=128, verbose_name="فرمت خروجی")
    memory_limit_kb = models.IntegerField(default=25600, verbose_name="محدودیت مموری")
    time_limit_ms = models.IntegerField(default=1000, verbose_name="محدودیت زمانی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    def __str__(self):
        return self.name


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name="سوال")
    input = models.TextField(verbose_name="ورودی")
    expected_output = models.TextField(verbose_name="خروجی قابل انتظار")
    is_sample = models.BooleanField(default=False, verbose_name="مثال است؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    class Meta:
        verbose_name = "تست کیس"
        verbose_name_plural = "تست کیس‌ها"

    def __str__(self):
        return self.problem.name


class Submission(models.Model):
    class StatusChoices(models.TextChoices):
        queued = ("Queued", "Queued")
        running = ("Running", "Running")
        done = ("Done", "Done")
        errors = ("Error", "Error")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name="سوال")
    language = models.ForeignKey(
        ProgrammingLanguage, on_delete=models.CASCADE, verbose_name="زبان برنامه‌نویسی"
    )
    source_code = models.TextField(verbose_name="کد")
    status = models.CharField(
        max_length=32, choices=StatusChoices.choices, verbose_name="وضعیت"
    )
    verdict = models.CharField(
        max_length=32, choices=VerdictChoices.choices, verbose_name="نتیجه"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "ارسال"
        verbose_name_plural = "ارسال‌ها"

    def __str__(self):
        return f"{self.user} --> {self.problem.name}"


class TestCaseResult(models.Model):
    submission = models.ForeignKey(
        Submission, on_delete=models.CASCADE, verbose_name="ارسال"
    )
    test_case = models.ForeignKey(
        TestCase, on_delete=models.CASCADE, verbose_name="تست کیس"
    )
    verdict = models.CharField(
        max_length=32, choices=VerdictChoices.choices, verbose_name="نتیجه"
    )
    time_ms = models.IntegerField(default=0, verbose_name="زمان")
    memory_kb = models.IntegerField(default=0, verbose_name="مموری")
    stdout = models.TextField(blank=True, default="", verbose_name="خروجی استاندارد")
    stderr = models.TextField(blank=True, default="", verbose_name="استاندارد ارور")
    exit_code = models.IntegerField(default=0, verbose_name="کد خطا")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "نتیحه تست کیس"
        verbose_name_plural = "نتایج تست کیس‌ها"

    def __str__(self):
        return f"{self.submission.problem} -->  {self.verdict}"


class ScoreAward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "problem"], name="unique_user_problem")
        ]
