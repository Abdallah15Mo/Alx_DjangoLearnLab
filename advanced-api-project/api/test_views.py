from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create authors and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(
            title="Harry Potter 1", publication_year=1997, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter 2", publication_year=1998, author=self.author
        )

        self.book_list_url = reverse(
            "book-list"
        )  # Make sure this matches your URL name
        self.book_detail_url = lambda pk: reverse("book-detail", args=[pk])

    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # update
    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "publication_year": 1999,
            "author": self.author.id,
        }
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    # delete
    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # filter
    def test_filter_books_by_year(self):
        response = self.client.get(self.book_list_url + "?publication_year=1997")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # order
    def test_order_books_by_title_desc(self):
        response = self.client.get(self.book_list_url + "?ordering=-title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(response.data[0]["title"], response.data[1]["title"])

    # search
    def test_search_books_by_title(self):
        response = self.client.get(self.book_list_url + "?search=Harry Potter 2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harry Potter 2")

    # permissions
    def test_anonymous_cannot_create_book(self):
        self.client.logout()
        data = {"title": "Anon Book", "publication_year": 2000, "author": self.author.id}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

