from modeltranslation.translator import TranslationOptions, register

from core.apps.bot.models import UserModel


@register(UserModel)
class UserTranslation(TranslationOptions):
    fields = []
