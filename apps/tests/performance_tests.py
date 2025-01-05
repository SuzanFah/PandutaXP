from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
import time

class PerformanceTestCase(TestCase):
    def test_service_listing_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('services-list'))
        execution_time = time.time() - start_time
        
        self.assertLess(execution_time, 0.5)
        self.assertEqual(response.status_code, 200)
