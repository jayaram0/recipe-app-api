"""
Test for django admin modifications
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Django admin tests"""

    def setUp(self):
        """Create User and Client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="testadmin@example.com", password="Test@123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com", password="Test.123", name="Test User"
        )

    def test_users_list(self):
        """Test the users list on admin page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user(self):
        """Test the user modifications"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user(self):
        """Test to create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
