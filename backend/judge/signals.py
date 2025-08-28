from django.db.models.signals import post_save
from django.dispatch import receiver
from judge.models import ProgrammingLanguage
from judge.core.utils import build_image


@receiver(post_save, sender=ProgrammingLanguage)
def build_language_image(sender, instance, created, **kwargs):
    if created or instance.dockerfile_path:
        build_image(instance)
