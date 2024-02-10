from  rest_framework.permissions import BasePermission
from user.models import UserRoles


class IsModerator(BasePermission):
    massage = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsLessonOwner(BasePermission):
    massage = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsCourseOwner(BasePermission):
    massage = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False