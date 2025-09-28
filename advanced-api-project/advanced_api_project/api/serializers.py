from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """Serializes all fields of the Book model"""
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """Custom validation to ensure publication_year is not in the future"""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Includes name field and nested BookSerializer for related books
    """
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']