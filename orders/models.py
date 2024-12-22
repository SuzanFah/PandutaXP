from django.db import models
from django.contrib.auth.models import User
from apps.clients.models import Client
from apps.providers.models import Provider

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('PICKUP', 'Out for Pickup'),
        ('PROCESSING', 'Processing'),
        ('DELIVERY', 'Out for Delivery'),
        ('COMPLETED', 'Completed')
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
