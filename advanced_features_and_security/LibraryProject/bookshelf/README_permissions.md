# Django Groups & Permissions Setup

This app uses Django’s built-in Groups and Permissions system to control access to books.

## Custom Permissions

Defined on the `Book` model:

- `can_view`: View a book list or detail
- `can_create`: Add new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

## Groups

Created via script or Django admin:

- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Enforcing Permissions

In `bookshelf/views.py`, permissions are enforced using:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
```
