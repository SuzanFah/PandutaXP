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

class ServiceManagementTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='servicemanager',
            password='testpass123'
        )
        self.provider = Provider.objects.create(
            user=self.user,
            phone='1234567890',
            address='456 Business Ave',
            service_type='Laundry & Dry Cleaning'
        )
        self.client = Client()
        self.client.login(username='servicemanager', password='testpass123')

    def test_add_service(self):
        service_data = {
            'name': 'Premium Dry Cleaning',
            'description': 'High-end garment care service',
            'price': '25.00',
            'duration': '48'
        }
        response = self.client.post(reverse('providers:add_service'), service_data)
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Service.objects.filter(name='Premium Dry Cleaning').exists())
        self.assertEqual(Service.objects.count(), 1)
