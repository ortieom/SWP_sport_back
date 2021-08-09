from rest_framework import permissions
from sport.models import Student


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'student') and request.user.student.student_status == 'Normal':
            return True
        return False


class SportSelected(IsStudent):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.student.sport


class IsTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'trainer')
