from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "user"
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")
