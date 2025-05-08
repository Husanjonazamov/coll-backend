from rest_framework import serializers

from core.apps.bot.models import UserModel


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            "id",
            "name",
        ]


class ListUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): ...


class RetrieveUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): ...


class CreateUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [
            "id",
            "name",
            "user_id"
        ]
