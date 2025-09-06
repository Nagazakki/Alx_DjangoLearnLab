from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # fields to display
    search_fields = ("title", "author")  # search functionality
    list_filter = ("publication_year",)  # filter sidebar
