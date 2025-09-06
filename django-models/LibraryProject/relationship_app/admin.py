# ===== SETTINGS.PY CONFIGURATION =====
# Add 'relationship_app' to your INSTALLED_APPS in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',  # Add this line
]

# ===== ADMIN.PY CONFIGURATION =====
# File: relationship_app/admin.py

from django.contrib import admin
from .models import Author, Book, Library, Librarian

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author']
    search_fields = ['title', 'author__name']
    ordering = ['title']

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']
    filter_horizontal = ['books']  # Makes ManyToMany easier to manage
    search_fields = ['name']
    ordering = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'library']
    list_filter = ['library']
    search_fields = ['name', 'library__name']
    ordering = ['name']