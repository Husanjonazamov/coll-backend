from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.bot.models import TeacherModel
from core.apps.bot.serializers.teacher import CreateTeacherSerializer, ListTeacherSerializer, RetrieveTeacherSerializer


from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class CustomPagination(PageNumberPagination):
    page_size = 100 
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "status": True,
            "data": {
                "links": {
                    "previous": self.get_previous_link(),
                    "next": self.get_next_link()
                },
                "total_items": self.page.paginator.count,
                "total_pages": math.ceil(self.page.paginator.count / self.page_size),
                "page_size": self.page_size,
                "current_page": self.page.number,
                "results": data
            }
        })






@extend_schema(tags=["teacher"])
class TeacherView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = ListTeacherSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination  

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTeacherSerializer,
        "retrieve": RetrieveTeacherSerializer,
        "create": CreateTeacherSerializer,
    }
