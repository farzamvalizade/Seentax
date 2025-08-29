from django.apps import AppConfig


class JudgeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "judge"

    verbose_name = "سیستم داروی"
    verbose_name_plural = "سیستم‌های داوری"

    def ready(self):
        import judge.signals
