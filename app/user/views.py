"""
Views for User API
"""
from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    searializer_class = UserSerializer
