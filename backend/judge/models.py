import os

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def dockerfile_upload_path(instance, filename):

    lang_name = instance.name.replace(" ", "_").lower()
    return os.path.join(f"{lang_name}_dockerfile", filename)


class VerdictChoices(models.TextChoices):
    accepted = ("Accepted", "AC")
    wrong_answer = ("Wrong Answer", "WA")
    time_limit_exceeded = ("Time Limit Exceeded", "TLE")
    memory_limit_exceeded = ("Memory Limit Exceeded", "MLE")
    runtime_error = ("Runtime Error", "RE")
    compile_error = ("Compile Error", "CE")


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    dockerfile_path = models.FileField(upload_to=dockerfile_upload_path)
    run_command = models.CharField(max_length=256)
    compile_command = models.CharField(max_length=256, blank=True, default="")
    need_compile = models.BooleanField(default=False)
    extension = models.CharField(max_length=128, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    class DifficultyChoices(models.TextChoices):
        easy = ("Easy", "Easy")
        normal = ("Normal", "Normal")
        hard = ("Hard", "Hard")

    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=16, choices=DifficultyChoices.choices)
    languages = models.ManyToManyField(ProgrammingLanguage)
    input_format = models.TextField(max_length=128)
    output_format = models.TextField(max_length=128)
    memory_limit_kb = models.IntegerField(default=256000)
    time_limit_ms = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Submission(models.Model):
    class StatusChoices(models.TextChoices):
        queued = ("Queued", "Queued")
        running = ("Running", "Running")
        done = ("Done", "Done")
        errors = ("Error", "Error")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    source_code = models.TextField()
    status = models.CharField(max_length=16, choices=StatusChoices.choices)
    verdict = models.CharField(max_length=32, choices=VerdictChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class TestCaseResult(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=32, choices=VerdictChoices.choices)
    time_ms = models.IntegerField(default=0)
    memory_kb = models.IntegerField(default=0)
    stdout = models.TextField(blank=True, default="")
    stderr = models.TextField(blank=True, default="")
    exit_code = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
