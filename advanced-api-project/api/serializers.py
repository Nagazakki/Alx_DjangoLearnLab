from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer handles serialization and deserialization of Book model instances.
    
    This serializer is responsible for:
    1. Converting Book model instances to JSON format for API responses
    2. Validating and converting JSON data to Book model instances for API requests
    3. Implementing custom validation rules for business logic
    
    Fields Serialized:
        - id: Primary key of the book (read-only, auto-generated)
        - title: The book's title (required, max 200 characters)
        - publication_year: Year of publication (required, integer with custom validation)
        - author: Foreign key to Author model (required for creation)
    
    Custom Validation:
        - publication_year: Ensures the year is not in the future to maintain data integrity
    
    Relationship Handling:
        The 'author' field represents the foreign key relationship to the Author model.
        When serializing (model to JSON), it shows the author's ID.
        When deserializing (JSON to model), it expects a valid author ID.
    """
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """
        Custom validation method for the publication_year field.
        
        Business Rule: Books cannot have a publication year in the future.
        This prevents data entry errors and maintains logical consistency.
        
        Args:
            value (int): The publication year to validate
            
        Returns:
            int: The validated publication year
            
        Raises:
            serializers.ValidationError: If the publication year is in the future
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer handles serialization and deserialization of Author model instances.
    
    This serializer implements a nested serialization approach to show the relationship
    between Authors and their Books. It demonstrates a one-to-many relationship where
    one author can have multiple books.
    
    Fields Serialized:
        - id: Primary key of the author (read-only, auto-generated)
        - name: The author's full name (required, max 100 characters)
        - books: Nested serialization of all books written by this author
    
    Relationship Handling:
        The 'books' field demonstrates the reverse foreign key relationship from
        Author to Book. This field uses the BookSerializer to provide full details
        of each book written by the author, creating a nested JSON structure.
        
        When an Author instance is serialized, it automatically includes all related
        books through the 'books' related_name defined in the Book model's ForeignKey.
        The nested BookSerializer ensures each book is fully serialized with all its fields.
        
        Example JSON output:
        {
            "id": 1,
            "name": "J.K. Rowling",
            "books": [
                {
                    "id": 1,
                    "title": "Harry Potter and the Philosopher's Stone",
                    "publication_year": 1997,
                    "author": 1
                },
                {
                    "id": 2,
                    "title": "Harry Potter and the Chamber of Secrets",
                    "publication_year": 1998,
                    "author": 1
                }
            ]
        }
    """
    
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']