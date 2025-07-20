from django.urls import path
from .views import register

urlpatterns = [
    # ... your other paths
    path("register/", register, name="register"),
]
