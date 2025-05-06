from django import forms

from core.apps.bot.models import CategoryModel


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = "__all__"
