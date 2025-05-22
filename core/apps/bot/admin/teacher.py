from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.bot.models import TeacherModel


@admin.register(TeacherModel)
class TeacherAdmin(ModelAdmin):
    list_display = (
        "id",
        "name"
    )
