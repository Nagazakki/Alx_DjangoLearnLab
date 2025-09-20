from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    
    # Secure search functionality - no SQL injection risk
    search_query = request.GET.get('search', '')
    if search_query:
        # Using Django ORM - automatically parameterized, safe from SQL injection
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query)
        )
    
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Secure input handling with validation
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        
        # Input validation
        if not title or not author:
            return render(request, 'bookshelf/book_create.html', 
                         {'error': 'Title and author are required'})
        
        if len(title) > 200 or len(author) > 100:
            return render(request, 'bookshelf/book_create.html',
                         {'error': 'Title or author too long'})
        
        # Safe ORM creation - no SQL injection risk
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    
    return render(request, 'bookshelf/book_create.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # Secure object retrieval
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        # Secure input handling with validation
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        
        # Input validation
        if not title or not author:
            return render(request, 'bookshelf/book_edit.html', 
                         {'book': book, 'error': 'Title and author are required'})
        
        if len(title) > 200 or len(author) > 100:
            return render(request, 'bookshelf/book_edit.html',
                         {'book': book, 'error': 'Title or author too long'})
        
        # Safe ORM update - no SQL injection risk
        book.title = title
        book.author = author
        book.save()
        return redirect('book_list')
    
    return render(request, 'bookshelf/book_edit.html', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # Secure object retrieval and deletion
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')