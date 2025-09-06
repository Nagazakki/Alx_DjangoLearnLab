# LibraryProject/relationship_app/urls.py

from django.urls import path
from .views import list_books, list_books_template, LibraryDetailView  # <-- explicit import

urlpatterns = [
    # Function-based view (plain text list of books)
    path('books/', list_books, name='book_list_text'),

    # Function-based view with template
    path('books/html/', list_books_template, name='book_list_html'),

    # Class-based view (detail page for a specific library)
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
