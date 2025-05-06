from django_filters import rest_framework as filters

from core.apps.bot.models import TeacherModel


class TeacherFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TeacherModel
        fields = [
            "name",
        ]
