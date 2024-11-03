""" module for the channel class """
from django.db import models
from .user import User

class Channel(models.Model):
    """ definition of the Channel class """
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    mentees = models.ManyToManyField(User, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    


