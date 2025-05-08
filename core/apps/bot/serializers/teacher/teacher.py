from rest_framework import serializers

from core.apps.bot.models import TeacherModel


class BaseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "description",
            "is_active"
        ]


class ListTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class RetrieveTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class CreateTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta):
        fields = [
            "id",
            "first_name",
        ]
