from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

USER_TYPE_CHOICES = (
    ('CLIENT', 'Client'),
    ('PROVIDER', 'Provider'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=[('CLIENT', 'Client'), ('PROVIDER', 'Provider')], default='CLIENT')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

