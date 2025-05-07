from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.bot.models import UserModel


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "user_id",
    )
