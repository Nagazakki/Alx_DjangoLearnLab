from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author and a book
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Book 1",
            publication_year=2020,
            author=self.author
        )

    def test_create_book_authenticated(self):
        # 🔑 Log in before making the request
        login = self.client.login(username="testuser", password="testpass")
        self.assertTrue(login)  # Check login succeeded

        response = self.client.post(
            "/books/create/",
            {"title": "Book 2", "publication_year": 2021, "author": self.author.id}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        # Don’t log in here
        response = self.client.post(
            "/books/create/",
            {"title": "Book 3", "publication_year": 2022, "author": self.author.id}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)