from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.bot.models import UserModel
from core.apps.bot.serializers.user import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer


@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListUserSerializer,
        "retrieve": RetrieveUserSerializer,
        "create": CreateUserSerializer,
    }
    
    def get_serializer_class(self):
        return self.action_serializer_class.get(self.action, ListUserSerializer)

    lookup_field = "user_id" 
    lookup_url_kwarg = "user_id"

    