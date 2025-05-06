from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CategoryModel(AbstractBaseModel):
    name = models.CharField(
        verbose_name=_("Nomi"),
        max_length=200,
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
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")
