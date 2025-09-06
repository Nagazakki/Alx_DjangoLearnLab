# relationship_app/query_samples.py
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

def list_books_in_library():
    # List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")

def retrieve_librarian_for_library():
    # Retrieve the librarian for a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

# Run the queries
if __name__ == "__main__":
    query_books_by_author()
    list_books_in_library()
    retrieve_librarian_for_library()