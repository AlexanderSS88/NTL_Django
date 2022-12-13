from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrRead(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user == obj.creator:
            return True


class AnyExceptTheOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.user != obj.creator) \
                and (request.user.is_authenticated):
            return True
