from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    # Other views (e.g., list_books, library_detail) can go below
    # path('books/', views.list_books, name='list_books'),
    # path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
    # Previous entries like login/register can also be here
]
from django.urls import path
from . import views

urlpatterns = [
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:pk>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", views.delete_book, name="delete_book"),
    # Include other views as needed
]
