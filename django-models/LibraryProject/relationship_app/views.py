from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view that returns a simple text list of book titles and authors
def list_books(request):
    books = Book.objects.select_related('author').all()
    # plain text list as the task requested
    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Optional function-based view that renders an HTML template
def list_books_template(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (DetailView) that shows a specific Library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # template will receive 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # include books in context (eager-load author to avoid extra queries)
        context['books'] = self.object.books.select_related('author').all()
        return context
