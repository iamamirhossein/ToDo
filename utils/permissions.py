from rest_framework.permissions import BasePermission
from account.models import Profile


class IsOwnerOfProfilePermission(BasePermission):
    def has_permission(self, request, view):
        profile_id = view.kwargs.get('pk')
        return Profile.objects.filter(pk=profile_id, user=request.user).exists()
