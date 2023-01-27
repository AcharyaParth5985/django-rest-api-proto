from rest_framework import serializers
from typing import Any


def BaseUserSerializer(klass: Any):
    class _klass(serializers.ModelSerializer):
        class Meta:
            model = klass
            exclude = ("is_staff", "is_superuser", "is_active")
            extra_kwargs = {"password": {"write_only": True}}

        def save(self, **kwargs):
            return self.Meta.model.objects.create_user(**self.validated_data)

    return _klass


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)


class UserChangePasswordSerialzer(serializers.Serializer):
    password1 = serializers.CharField(allow_blank=False)
    password2 = serializers.CharField(allow_blank=False)
