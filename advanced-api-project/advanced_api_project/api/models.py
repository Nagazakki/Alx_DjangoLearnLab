from django.db import models

class Author(models.Model):
    """
    Author model represents book authors in the library system.
    
    This model stores basic information about authors and serves as the 'one' side
    in a one-to-many relationship with the Book model. Each author can have
    multiple books, but each book has only one primary author.
    
    Fields:
        name (CharField): The full name of the author. Maximum length of 100 characters.
                         This field is required and cannot be null.
    
    Relationships:
        books: Reverse relationship to Book model through the 'author' foreign key.
               Accessible via author.books.all() to get all books by this author.
    
    Meta Options:
        ordering: Authors are ordered alphabetically by name by default.
    """
    name = models.CharField(max_length=100, help_text="Full name of the author")

    def __str__(self):
        """
        String representation of the Author model.
        Returns the author's name for display purposes.
        """
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    """
    Book model represents individual books in the library system.
    
    This model stores essential information about books and establishes a 
    many-to-one relationship with the Author model. Multiple books can be
    written by the same author, but each book has only one primary author.
    
    Fields:
        title (CharField): The title of the book. Maximum length of 200 characters.
                          This field is required and cannot be null.
        publication_year (IntegerField): The year the book was published.
                                       Must be a valid integer year.
        author (ForeignKey): Foreign key relationship to the Author model.
                           Establishes the many-to-one relationship where multiple
                           books can belong to one author. Uses CASCADE deletion,
                           meaning if an author is deleted, all their books are
                           also deleted.
    
    Relationships:
        author: Many-to-one relationship with Author model. Each book belongs
                to exactly one author. The related_name 'books' allows reverse
                lookup from Author to Books (author.books.all()).
    
    Meta Options:
        ordering: Books are ordered alphabetically by title by default.
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        help_text="The author who wrote this book"
    )

    def __str__(self):
        """
        String representation of the Book model.
        Returns the book's title for display purposes.
        """
        return f"{self.title} ({self.publication_year})"

    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"