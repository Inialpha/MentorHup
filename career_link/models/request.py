""" module for the channel class """
from django.db import models
from .user import User
from .channel import Channel

class Request(models.Model):
    """ definition of the Request class """
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, default="pending")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
