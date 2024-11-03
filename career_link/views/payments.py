from rest_framework import viewsets
from ..models.payment import Payment
from ..serializers.paymentSerializer import PaymentSerializer
from rest_framework.response import Response

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
