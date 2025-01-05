from django.test import TestCase
from django.contrib.auth.models import User
from .models import Provider

class ProviderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testprovider',
            password='testpass123'
        )
        self.provider = Provider.objects.create(
            user=self.user,
            phone='1234567890',
            address='123 Provider St',
            service_type='Laundry'
        )

    def test_service_creation(self):
        # Test service creation logic
