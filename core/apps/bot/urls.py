from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.bot.views import (
    CategoryView,
    TeacherView
)

router = DefaultRouter()
router.register(r"category", CategoryView, basename="category")
router.register(r"teacher", TeacherView, basename="teacher")

urlpatterns = [
    path("", include(router.urls)),
]
