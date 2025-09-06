# relationship_app/models.py
from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey to Author - Many books can belong to one author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=150)
    # ManyToManyField to Book - A library can have many books, books can be in many libraries
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Libraries"

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField to Library - Each librarian manages exactly one library
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name