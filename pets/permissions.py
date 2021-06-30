"""Pets permissions."""
from rest_framework import permissions


class PetPermission(permissions.BasePermission):
    """Pet permissions."""

    SAFE_METHODS = ("GET", "HEAD", "OPTIONS",)

    def has_object_permission(self, request, view, obj) -> bool:
        """Check pet permission."""
        user = request.user
        if request.method in self.SAFE_METHODS:
            return True
        return user == obj.owner
