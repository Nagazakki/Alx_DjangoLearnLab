from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Create sample author and book
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Book 1",
            publication_year=2020,
            author=self.author
        )

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")  

        response = self.client.post(
            "/books/create/",
            {"title": "Book 2", "publication_year": 2021, "author": self.author.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.data["title"], "Book 2")
        self.assertEqual(response.data["publication_year"], 2021)

    def test_get_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])
        self.assertEqual(response.data[0]["title"], "Book 1")