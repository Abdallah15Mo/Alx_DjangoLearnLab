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
