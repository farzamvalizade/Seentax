from django.contrib.auth import get_user_model

from rest_framework import serializers

from judge.models import Problem, ProgrammingLanguage

User = get_user_model()


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "is_staff", "is_superuser")


class ProblemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            "name",
            "description",
            "difficulty",
            "languages",
            "input_format",
            "output_format",
            "memory_limit_kb",
            "time_limit_ms",
            "created_at",
            "updated_at",
        )


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ["id", "name", "extension", "need_compile"]
