from django.db import models
from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Custom permission to only allow users to access the API.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'User'
    

class IsAdminOrSuperadmin(permissions.BasePermission):
    """
    Custom permission to only allow admin or superadmin to access the API.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == 'Admin' or request.user.is_superuser)