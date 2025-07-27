# Register your models here.
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns in the list view
    list_filter = ("author", "publication_year")  # filters on the right
    search_fields = ("title", "author")  # search bar


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff")

    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )


# ✅ This is the line being checked:
admin.site.register(CustomUser, CustomUserAdmin)
