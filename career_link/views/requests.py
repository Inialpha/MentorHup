from rest_framework import viewsets
from ..models.request import Request
from ..serializers.requestSerializer import RequestSerializer
from rest_framework.response import Response

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
