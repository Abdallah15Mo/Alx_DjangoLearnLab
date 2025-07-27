from django.shortcuts import render

# Create your views here.
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    # Logic to handle book creation
    pass


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Logic to handle editing
    pass


@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    # Redirect


# ✅ GOOD: Django ORM escapes input
from django.db.models import Q


def book_search(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, "bookshelf/book_list.html", {"books": books})


# views.py
from django.http import HttpResponse


def secure_view(request):
    response = HttpResponse("Secure content")
    response["Content-Security-Policy"] = "default-src 'self'"
    return response


# SECURITY: Prevent browser-based XSS attacks
SECURE_BROWSER_XSS_FILTER = True
