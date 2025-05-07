from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.bot.models import UserModel


@receiver(post_save, sender=UserModel)
def UserSignal(sender, instance, created, **kwargs): ...
