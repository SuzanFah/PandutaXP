from django.test import TestCase
from .models import Order

class OrderTests(TestCase):
    def test_create_order(self):
        order = Order.objects.create(
            service_type='wash_and_fold',
            items={'shirts': 2, 'pants': 3},
            pickup_time='2024-01-15T10:00:00Z'
        )
        self.assertEqual(order.service_type, 'wash_and_fold')
