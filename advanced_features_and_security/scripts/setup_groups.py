# scripts/setup_groups.py
from django.contrib.auth.models import Group, Permission
from django.apps import apps


def run():
    Book = apps.get_model("bookshelf", "Book")

    permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for codename in perms:
            perm = Permission.objects.get(codename=codename, content_type__model="book")
            group.permissions.add(perm)
