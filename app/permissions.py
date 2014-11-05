from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Permisos de lectura son permitidos a cualquier petición (request)
        # asi que permitimos a las peticiones con métodos GET, HEAD o OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permisos de escritura son solo permitidos a dueños del objeto.
        return obj.owner == request.user