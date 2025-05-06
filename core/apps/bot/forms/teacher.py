from django import forms

from core.apps.bot.models import TeacherModel


class TeacherForm(forms.ModelForm):

    class Meta:
        model = TeacherModel
        fields = "__all__"
