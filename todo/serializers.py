from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    reporter = serializers.HiddenField(source=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = ("title", "description", "assigned", "item_type", "status",)
