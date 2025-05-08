from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.bot.models import UserModel
from core.apps.bot.serializers.user import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer


@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListUserSerializer,
        "retrieve": RetrieveUserSerializer,
        "create": CreateUserSerializer,
    }
    