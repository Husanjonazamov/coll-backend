from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.bot.models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
