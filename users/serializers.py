from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)


    def validate_email(self, value: str):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError("This field must be unique.")
        except User.DoesNotExist:
            return value
