from django.db import models
from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Custom permission to only allow candidates to access the API.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'User'