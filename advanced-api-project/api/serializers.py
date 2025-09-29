from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation for publication_year
    to ensure it is not set in the future.
    """
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.
    Includes a nested BookSerializer to represent related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
