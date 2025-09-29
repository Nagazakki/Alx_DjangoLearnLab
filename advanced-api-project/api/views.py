from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


@api_view(["GET"])
def author_list(request):
    """
    Returns all authors with their nested books.
    """
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def book_list(request):
    """
    Returns all books with validation applied.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
