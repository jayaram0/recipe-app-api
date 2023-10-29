"""
Database Models
Author: Jayaram
"""
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Managers  for Users"""

    def create_user(self, email, password=None, **extra_field):
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system
    """

    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
