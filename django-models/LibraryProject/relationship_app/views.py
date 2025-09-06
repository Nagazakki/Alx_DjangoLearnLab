from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView
from .models import Book, Library, Author, Librarian

# Function-based view that lists all books
def list_books(request):
    books = Book.objects.all()  # <-- expected pattern
    # plain text list
    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Optional function-based view that renders HTML template
def list_books_template(request):
    books = Book.objects.all()  # <-- expected pattern
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # safe, and matches pattern
        return context
