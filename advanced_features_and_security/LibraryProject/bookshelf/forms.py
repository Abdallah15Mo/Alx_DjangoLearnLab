# bookshelf/forms.py

from django import forms


class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
