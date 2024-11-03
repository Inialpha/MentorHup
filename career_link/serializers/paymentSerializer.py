# serializers.py
from rest_framework import serializers
from ..models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'created_at', 'user', 'description', 'payment_method', 'amount']
        extra_kwargs = {
            'user': {'required': False},
            'description': {'required': False},
            'payment_method': {'required': False},
            'amount': {'required': False}
        }

    def create(self, validated_data):
        required_fields = ['amount', 'user', 'payment_method']
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError({field: ['This field is required.']})

        return Payment.objects.create(**validated_data)

