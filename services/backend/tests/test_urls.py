"""
Simple tests for the django backend.
"""
from django.test import TestCase


class BaseTest(TestCase):
    def test_base_admin_page(self):
        """Checks if the base admin page returns a 301."""
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, 302)

    def test_renders_tools_page(self):
        """Checks if the tools page renders."""
        response = self.client.get("/tools")
        self.assertEqual(response.status_code, 200)

    def test_renders_roles_page(self):
        """Checks if the roles page renders."""
        response = self.client.get("/roles")
        self.assertEqual(response.status_code, 200)

    def test_renders_repos_page(self):
        """Checks if the repos page renders."""
        response = self.client.get("/repos")
        self.assertEqual(response.status_code, 200)

    def test_renders_homepage(self):
        """Checks if the repos page renders."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
