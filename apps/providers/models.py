from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    services = models.TextField()  # Using TextField instead of JSONField
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.business_name