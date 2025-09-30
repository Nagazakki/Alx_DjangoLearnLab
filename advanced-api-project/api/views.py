from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="tester", password="password123")

        # Authenticated client
        self.client = APIClient()
        self.client.login(username="tester", password="password123")

        # Create some books
        self.book1 = Book.objects.create(title="Django Unchained", author=self.user, publication_year=2012)
        self.book2 = Book.objects.create(title="Python 101", author=self.user, publication_year=2020)
        self.book3 = Book.objects.create(title="Advanced Django", author=self.user, publication_year=2018)

        self.list_url = reverse("book-list")  # comes from BookListView
        # For detail endpoints we’ll reverse dynamically

    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        """Test creating a book while logged in"""
        data = {"title": "New Book", "author": self.user.id, "publication_year": 2021}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        """Test unauthenticated users cannot create"""
        client = APIClient()  # no login
        data = {"title": "Unauthorized Book", "author": self.user.id, "publication_year": 2021}
        response = client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book"""
        url = reverse("book-detail", args=[self.book1.id])
        data = {"title": "Updated Title", "author": self.user.id, "publication_year": 2015}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book"""
        url = reverse("book-detail", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_filter_books_by_year(self):
        """Test filtering works"""
        response = self.client.get(self.list_url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python 101")

    def test_search_books(self):
        """Test searching by title"""
        response = self.client.get(self.list_url, {"search": "Django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        """Test ordering"""
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))