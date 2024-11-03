from rest_framework import viewsets
from ..models.user import User
from ..models.channel import Channel
from ..serializers.channelSerializer import ChannelSerializer
from rest_framework.response import Response

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
