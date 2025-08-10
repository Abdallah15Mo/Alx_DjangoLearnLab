from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Author(models.Model):
    """
    Author model represents the writer of books.
    One Author can write multiple books.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an Author.
    Each book has a title, publication year, and is linked to one Author.
    """

    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ✅ List all books (read-only)
class BookListView(generics.ListAPIView):
    """
    GET: Returns a list of all books.
    Accessible to any user (read-only).
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Returns details of a single book by ID.
    Accessible to any user.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update a book's details.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book from the database.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


from django.contrib.auth.models import User


class Book(models.Model):
    ...
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
