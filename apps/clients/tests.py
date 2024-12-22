from django.test import TestCase, Client as TestClient
from django.urls import reverse
from django.contrib.auth.models import User
from apps.clients.models import Client

class ClientDashboardTest(TestCase):
    def setUp(self):
        self.test_client = TestClient()
        self.user = User.objects.create_user(
            username='testclient',
            password='testpass123'
        )
        self.client_profile = Client.objects.create(
            user=self.user,
            phone='1234567890',
            address='123 Test St'
        )

    def test_dashboard_access(self):
        # Test direct dashboard access
        self.test_client.login(username='testclient', password='testpass123')
        response = self.test_client.get(reverse('client_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_content(self):
        # Test dashboard displays correct user info
        self.test_client.login(username='testclient', password='testpass123')
        response = self.test_client.get(reverse('client_dashboard'))
        self.assertContains(response, 'testclient')

# Add more functionality tests
def test_order_creation(self):
    # Implement order placement
    # Add service selection
    # Implement pricing calculation
