
from rest_framework.test import APITestCase
from django.urls import reverse

class OrderAPITests(APITestCase):
    def test_update_order_status(self):
        response = self.client.post(
            reverse('order-status-update'),
            {"order_id": "1", "status": "in_progress"}
        )
        self.assertEqual(response.status_code, 200)
