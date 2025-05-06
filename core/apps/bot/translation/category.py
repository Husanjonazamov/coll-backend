from modeltranslation.translator import TranslationOptions, register

from core.apps.bot.models import CategoryModel


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = []
