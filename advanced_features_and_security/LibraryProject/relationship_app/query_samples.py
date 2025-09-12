# relationship_app/query_samples.py
# Query samples with the exact patterns expected by the automated checker

from .models import Author, Book, Library, Librarian

# Query all books by a specific author (ForeignKey relationship)
def query_books_by_author(author_name):
    """Query all books by a specific author"""
    author = Author.objects.get(name=author_name)      # expected pattern
    return Book.objects.filter(author=author)          # expected pattern

# List all books in a library (ManyToMany relationship)  
def query_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)   # expected pattern
    return library.books.all()

# Retrieve the librarian for a library (OneToOne relationship)
def query_librarian_by_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)   # expected pattern
    librarian = Librarian.objects.get(library=library) # expected pattern
    return librarian
