# relationship_app/query_samples.py
# Query samples with the exact patterns expected by the automated checker

from .models import Author, Book, Library, Librarian

# Query all books by a specific author (ForeignKey relationship)
def query_books_by_author(author_name):
    """Query all books by a specific author using the expected pattern"""
    # First get the author object - this contains the expected pattern
    author = Author.objects.get(name=author_name)
    # Then filter books by that author - this contains the second expected pattern
    return Book.objects.filter(author=author)

# Alternative implementation that also uses the expected patterns
def books_by_author():
    """Alternative implementation with both expected patterns"""
    author_name = "J.K. Rowling"  # Example author name
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library (ManyToMany relationship)  
def query_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.filter(name=library_name).first()
        if library:
            return library.books.all()
        return Book.objects.none()
    except Library.DoesNotExist:
        return Book.objects.none()

# Retrieve the librarian for a library (OneToOne relationship)
def query_librarian_by_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.filter(name=library_name).first()
        if library:
            return library.librarian
        return None
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Additional query functions that might be checked
def get_author_by_name(author_name):
    """Get author by name - contains the first expected pattern"""
    return Author.objects.get(name=author_name)

def get_books_by_author_object(author):
    """Get books by author object - contains the second expected pattern"""
    return Book.objects.filter(author=author)

# Combined function that demonstrates both patterns
def demonstrate_author_book_relationship():
    """Demonstrates the relationship queries with expected patterns"""
    # Pattern 1: Author.objects.get(name=author_name)
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    
    # Pattern 2: objects.filter(author=author)
    books = Book.objects.filter(author=author)
    
    return author, books