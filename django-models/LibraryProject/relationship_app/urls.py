# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Function-based view (plain text list of books)
    path('books/', views.list_books, name='book_list_text'),

    # Function-based view with template
    path('books/html/', views.list_books_template, name='book_list_html'),

    # Class-based view (detail page for a specific library)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
