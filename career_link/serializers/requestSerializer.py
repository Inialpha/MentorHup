# serializers.py
from rest_framework import serializers
from ..models.user import User
from ..models.channel import Channel
from ..models.request import Request

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ['id', 'created_at', 'sender', 'channel', 'status']
        extra_kwargs = {
            'sender': {'required': False},
            'channel': {'required': False},
            'status': {'required': False},
        }

    def create(self, validated_data):
        required_fields = ['sender', 'channel']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        return Request.objects.create(**validated_data)

