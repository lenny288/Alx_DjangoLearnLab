
import django
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Clear previous data (optional, for repeated testing)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create sample data
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George R.R. Martin")

book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
book3 = Book.objects.create(title="A Game of Thrones", author=author2)

library1 = Library.objects.create(name="City Library")
library2 = Library.objects.create(name="University Library")

library1.books.add(book1, book3)
library2.books.add(book2)

librarian1 = Librarian.objects.create(name="Alice", library=library1)
librarian2 = Librarian.objects.create(name="Bob", library=library2)

# Sample Queries

print("=== All books by J.K. Rowling ===")
books_by_rowling = Book.objects.filter(author=author1)
for book in books_by_rowling:
    print(f"- {book.title}")

print("\n=== All books in City Library ===")
for book in library1.books.all():
    print(f"- {book.title}")

print("\n=== Librarian for City Library ===")
print(library1.librarian.name)

print("\n=== Librarian for University Library ===")
print(library2.librarian.name)
