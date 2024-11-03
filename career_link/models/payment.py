""" module for the channel class """
from django.db import models
from .user import User


class Payment(models.Model):
    """ definition of the Channel class """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
