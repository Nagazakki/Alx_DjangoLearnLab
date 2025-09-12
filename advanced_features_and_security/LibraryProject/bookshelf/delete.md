from bookshelf.models import Book

# Delete the book you created and confirm the deletion by trying to retrieve all books again
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
all_books = Book.objects.all()
print(f"All books after deletion: {list(all_books)}")