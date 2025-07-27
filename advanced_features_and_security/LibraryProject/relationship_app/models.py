# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model with custom permissions
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]


# Library model with ManyToMany relationship to Book
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField("Book", through="LibraryBook")

    def __str__(self):
        return self.name


# Intermediate model for the ManyToMany relationship
class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.library.name} - {self.book.title}"


# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Extended User model with role
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
