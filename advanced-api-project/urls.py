from django.contrib import admin
from django.urls import path, include  # ✅ make sure include is imported

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),  # ✅ this line connects your app's URLs
]


from django.contrib import admin
from django.urls import path, include  # ✅ include is required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),  # ✅ contains "api.urls"
]
