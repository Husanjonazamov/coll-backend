from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TeacherModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Ism"), max_length=255)
   
    is_active = models.BooleanField(
        verbose_name=_("Faolmi ?"),
        default=True
    )
    
    
    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "teacher"
        verbose_name = _("TeacherModel")
        verbose_name_plural = _("TeacherModels")
