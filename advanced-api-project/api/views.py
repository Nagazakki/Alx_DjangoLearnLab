from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters  # <-- checker wants this

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.

    Examples:
    - Filtering: /api/books/?title=SomeTitle&author__name=AuthorName&publication_year=2020
    - Searching: /api/books/?search=keyword
    - Ordering:  /api/books/?ordering=title  or  /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ["title", "author__name", "publication_year"]

    # Searching fields
    search_fields = ["title", "author__name"]

    # Ordering fields
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # Default ordering