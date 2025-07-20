from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_orwell = Book.objects.filter(author=author)
print("Books by George Orwell:")
for book in books_by_orwell:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
