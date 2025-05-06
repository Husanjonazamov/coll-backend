from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.bot.models import TeacherModel


@receiver(post_save, sender=TeacherModel)
def TeacherSignal(sender, instance, created, **kwargs): ...
