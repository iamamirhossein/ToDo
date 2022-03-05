from rest_framework import serializers
from rest_framework import exceptions
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nick_name', 'avatar',)

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        validated_data["user"] = user
        try:
            Profile(**validated_data).save()
            return Profile(**validated_data)
        except Exception as ex:
            raise exceptions.ValidationError(str(ex))
