from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to view, edit, or delete it.
    """

    def has_permission(self, request, view):
        # Allow all users to list or create categories (GET or POST)
        if request.method in ['GET', 'POST']:
            return True
        # For other methods, proceed to has_object_permission
        return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the category or an admin.
        return obj.user == request.user or request.user.is_staff
