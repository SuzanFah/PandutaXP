
from django.test import TestCase
from django.urls import reverse
from apps.orders.models import Order

class OrderTests(TestCase):
    def setUp(self):
        self.order_data = {
            "service_type": "laundry",
            "items": ["shirts", "pants"],
            "pickup_time": "2024-01-06T13:00:00Z"
        }

    def test_create_order(self):
        response = self.client.post(
            reverse('order-create'),
            self.order_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
