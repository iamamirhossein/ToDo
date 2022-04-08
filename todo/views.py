from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_permissions(self):
        if self.action == "destroy":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

