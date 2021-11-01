
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsCreator(IsAuthenticated):

    def has_permission(self, request, view):
        breakpoint()
        return True
        # return bool(
        #     request.user and request.user.is_staff
        #     and (request.user.is_superuser or request.user == )
        # )
        