from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner


class IsAuthCreate(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST" and request.user.is_authenticated:
            return True
        elif request.method == "POST" and not request.user.is_authenticated:
            return False
        elif request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner


class IsOwnerOrModerator(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST" and request.user.role in ["user"]:
            return True
        elif request.method in ["PUT", "PATCH"] and request.user.role in ["user", "moderator"]:
            return True
        elif request.method == "DELETE" and request.user.role in ["user"]:
            return True
        elif request.method in SAFE_METHODS and request.user.role in ["user", "moderator"]:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == "moderator":
            return True
        elif request.user.role == "user":
            return request.user == obj.owner
