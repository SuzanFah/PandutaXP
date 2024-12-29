from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    service_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.provider.user.username}"
        return self.user.username

class Service(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Duration in minutes')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.provider.user.username}"        