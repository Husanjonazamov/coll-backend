from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.bot.models import TeacherModel
from core.apps.bot.serializers.teacher import CreateTeacherSerializer, ListTeacherSerializer, RetrieveTeacherSerializer

@extend_schema(tags=["teacher"])
class TeacherView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = ListTeacherSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTeacherSerializer,
        "retrieve": RetrieveTeacherSerializer,
        "create": CreateTeacherSerializer,
    }
