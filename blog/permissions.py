from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allowing the read access to all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # only we are  allowing write access if the user is the owner of the BlogPost
        return obj.author == request.user