"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
import unittest


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)  # add assertion here
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for user"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for mail, expected in sample_emails:
            user = get_user_model().objects.create_user(mail, "Sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_value_error(self):
        """Test that creating user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "Sample123")

    def test_create_superuser(self):
        """Test to create a superuser"""
        user = get_user_model().objects.create_superuser("test@example.com", "Test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
