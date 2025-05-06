from modeltranslation.translator import TranslationOptions, register

from core.apps.bot.models import TeacherModel


@register(TeacherModel)
class TeacherTranslation(TranslationOptions):
    fields = []
