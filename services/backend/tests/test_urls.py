"""
Simple tests for the django backend.
"""
from django.test import TestCase

class BaseTest(TestCase):

    def test_base_admin_page(self):
        """Checks if the base admin page returns a 301."""
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 301)

