from django.db import models
from apps.clients.models import Client

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField()
    service_type = models.CharField(max_length=100)
    items = models.TextField(blank=True)  # Keeping existing field

    def __str__(self):
        return f"Order {self.id} - {self.client.user.username}"