from django.views.generic import ListView as DjangoListView, DetailView as DjangoDetailView
from django.views.generic.edit import CreateView as DjangoCreateView, UpdateView as DjangoUpdateView, DeleteView as DjangoDeleteView
from .models import Book


class ListView(DjangoListView):
    model = Book
    template_name = "books/book_list.html"  # required for Django CBVs
    context_object_name = "books"


class DetailView(DjangoDetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class CreateView(DjangoCreateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "books/book_form.html"
    success_url = "/books/"


class UpdateView(DjangoUpdateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "books/book_form.html"
    success_url = "/books/"


class DeleteView(DjangoDeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = "/books/"