from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TeacherModel(AbstractBaseModel):
    first_name = models.CharField(verbose_name=_("Ism"), max_length=255)
    category = models.ForeignKey(
        "bot.CategoryModel",
        on_delete=models.CASCADE,
        related_name="teacher",
        verbose_name=_("Kategoriya"),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Familya"),
        max_length=255,
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        verbose_name=_("Yosh"),
        default=0,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_("Tavsif"),
        null=True,
        blank=True
    )
    
    
    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "teacher"
        verbose_name = _("TeacherModel")
        verbose_name_plural = _("TeacherModels")
