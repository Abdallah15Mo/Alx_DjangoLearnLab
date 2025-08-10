from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser  # 👈 Add this here
from .models import Book
from .serializers import BookSerializer


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book instance.
    Automatically assigns the logged-in user as creator.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # This is where you customize save logic
        serializer.save(created_by=self.request.user)


