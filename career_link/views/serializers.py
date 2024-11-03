# serializers.py
from rest_framework import serializers
from ..models.user import User
from ..models.channel import Channel


class UserSerializer(serializers.ModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['id', 'email', 'created_at', "bio", "firstname", "lastname", "role", "categories"]
        extra_kwargs = {
            'email': {'required': False},
            'bio': {'required': False},
            'firstname': {'required': False},
            'lastname': {'required': False},
            'role': {'required': False},
            'categories': {'required': False}  # Assuming categories is optional
        }

    def create(self, validated_data):
        # Only enforce required fields during POST request
        required_fields = ['email', 'firstname', 'lastname', 'role']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        return User.objects.create(**validated_data)


class ChannelSerializer(serializers.ModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

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
        print(validated_data)
        required_fields = ['name', 'mentor']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        mentees_list = validated_data.pop('mentees')
        channel = Channel.objects.create(**validated_data)
        channel.mentees.set(mentees_list)
        return channel

