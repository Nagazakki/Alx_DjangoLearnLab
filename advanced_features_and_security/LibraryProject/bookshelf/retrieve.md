from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")

print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")