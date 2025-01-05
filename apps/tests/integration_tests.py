from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.providers.models import Provider, Service
from apps.clients.models import Client, Order

class OrderFlowTestCase(TestCase):
    def setUp(self):
        # Create provider user and profile
        self.provider_user = User.objects.create_user(
            username='testprovider',
            password='providerpass123'
        )
        self.provider = Provider.objects.create(
            user=self.provider_user,
            phone='1234567890',
            address='789 Laundry St',
            service_type='Full Service Laundry'
        )
        
        # Create client user and profile
        self.client_user = User.objects.create_user(
            username='testclient',
            password='clientpass123'
        )
        self.client_profile = Client.objects.create(
            user=self.client_user,
            phone='0987654321',
            address='321 Client Ave'
        )
        
        # Create a service
        self.service = Service.objects.create(
            provider=self.provider,
            name='Express Wash',
            price='15.00',
            duration='24'
        )
        
        self.client = Client()

    def test_complete_order_flow(self):
        # Client login and order creation
        self.client.login(username='testclient', password='clientpass123')
        order_data = {
            'service': self.service.id,
            'pickup_date': '2024-01-20',
            'special_instructions': 'Handle with care'
        }
        response = self.client.post(reverse('clients:create_order'), order_data)
        self.assertEqual(response.status_code, 302)
        
        # Provider handling order
        self.client.login(username='testprovider', password='providerpass123')
        order = Order.objects.first()
        update_data = {
            'order_id': order.id,
            'status': 'in_progress'
        }
        response = self.client.post(reverse('providers:update_order_status'), update_data)
        self.assertEqual(response.status_code, 200)
