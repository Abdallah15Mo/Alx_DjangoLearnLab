# relationship_app/views.py
from django.shortcuts import render
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: auto login after registration
            return redirect("list_books")  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")  # or 'list_books' if you prefer
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile


def role_required(role):
    def check(user):
        return hasattr(user, "userprofile") and user.userprofile.role == role

    return user_passes_test(check)


@login_required
@role_required("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@login_required
@role_required("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@login_required
@role_required("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")
