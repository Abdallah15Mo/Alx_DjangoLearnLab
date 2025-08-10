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
