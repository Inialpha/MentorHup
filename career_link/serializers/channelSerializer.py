# serializers.py
from rest_framework import serializers
from ..models.channel import Channel
from ..models.user import User


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ['id', 'created_at', 'mentor', 'name', 'description', 'mentees', 'price']
        extra_kwargs = {
            'mentor': {'required': False},
            'name': {'required': False},
            'description': {'required': False},
            'mentees': {'required': False},
            'price': {'required': False},
        }

    def create(self, validated_data):
        required_fields = ['name', 'mentor']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        mentees_list = validated_data.pop('mentees')
        channel = Channel.objects.create(**validated_data)
        channel.mentees.set(mentees_list)
        return channel

