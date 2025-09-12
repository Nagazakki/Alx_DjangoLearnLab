from bookshelf.models import Book

# Create a Book instance with title "1984", author "George Orwell", and publication year 1949
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(f"Book created successfully: {book}")