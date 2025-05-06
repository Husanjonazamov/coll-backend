from rest_framework import serializers

from core.apps.bot.models import TeacherModel


class BaseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = [
            "id",
            "name",
        ]


class ListTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class RetrieveTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta): ...


class CreateTeacherSerializer(BaseTeacherSerializer):
    class Meta(BaseTeacherSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
