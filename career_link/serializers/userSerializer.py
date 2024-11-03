# serializers.py
from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'created_at', "bio", "first_name", "last_name", "role", "categories", "password"]
        extra_kwargs = {
            'email': {'required': False},
            'bio': {'required': False},
            'firs_tname': {'required': False},
            'last_name': {'required': False},
            'role': {'required': False},
            'categories': {'required': False}  # Assuming categories is optional
        }

    def create(self, validated_data):
        # Only enforce required fields during POST request
        required_fields = ['email', 'first_name', 'last_name', 'role', 'password']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        return User.objects.create(**validated_data)
