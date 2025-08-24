from django.contrib import admin
from .models import ProgrammingLanguage, Submission, Problem, TestCase, TestCaseResult


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "extension", "need_compile", "created_at")
    search_fields = ("name",)


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty", "memory_limit_kb", "time_limit_ms", "created_at", "updated_at")
    list_editable = ("difficulty", "memory_limit_kb", "time_limit_ms")
    search_fields = ("name",)
    list_filter = ("difficulty", )


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ("problem", "is_sample", "created_at", "updated_at")
    list_editable = ("is_sample",)
    search_fields = ("problem__name",)
    list_filter = ("is_sample", "problem")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "problem", "language", "created_at", "status", "verdict", "created_at")
    list_editable = ("language", "status", "verdict")
    search_fields = ("problem__name",)
    list_filter = ("language", "status", "verdict", "problem")


@admin.register(TestCaseResult)
class TestCaseResultAdmin(admin.ModelAdmin):
    list_display = ("test_case", "verdict", "time_ms", "memory_kb", "exit_code")
    list_editable = ("time_ms", "memory_kb", "exit_code")
