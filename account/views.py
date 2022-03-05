from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOfProfilePermission
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwnerOfProfilePermission]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
