from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Ism"), max_length=255)
    user_id = models.BigIntegerField(
        verbose_name=_("Telegram id"),
        default=0,
        unique=True,
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "user"
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")
