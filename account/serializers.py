from rest_framework import serializers
from rest_framework import exceptions
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    is_created = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ('nick_name', 'avatar', 'is_created',)

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        validated_data["user"] = user
        try:
            instance, is_created = Profile.objects.get_or_create(**validated_data)
            instance.is_created = is_created
            return instance
        except Exception as ex:
            raise exceptions.ValidationError(str(ex))
