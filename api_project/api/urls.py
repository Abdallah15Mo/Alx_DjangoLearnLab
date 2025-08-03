from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# DRF Router for CRUD operations
router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    # Read-only list view
    path("books/", BookList.as_view(), name="book-list"),
    # Include router-generated routes
    path("", include(router.urls)),
]
