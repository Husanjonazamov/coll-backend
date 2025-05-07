from django import forms

from core.apps.bot.models import UserModel


class UserForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = "__all__"
