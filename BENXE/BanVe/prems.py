from rest_framework import permissions

class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return elf.has_permission(request, view) and request.user == obj.user