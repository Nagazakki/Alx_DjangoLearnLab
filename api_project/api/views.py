from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()              # all books from the database
    serializer_class = BookSerializer          # use the BookSerializer
