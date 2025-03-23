import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from books.models import Book

@pytest.mark.django_db
def test_book_creation():
    """
    Test book creation by an authenticated user.
    """
    client = APIClient()
    user = User.objects.create_superuser(username="admin", email="admin@example.com", password="adminpass")
    client.force_authenticate(user=user)
    
    response = client.post("/api/books/", {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "published_date": "1949-06-08"
    })
    
    assert response.status_code == 201
    assert response.data["title"] == "1984"

@pytest.mark.django_db
def test_get_books():
    """
    Test retrieving books.
    """
    client = APIClient()
    user = User.objects.create_superuser(username="admin", email="admin@example.com", password="adminpass")
    client.force_authenticate(user=user)

    Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565")

    response = client.get("/api/books/")
    
    assert response.status_code == 200
    assert len(response.data) > 0

@pytest.mark.django_db
def test_book_not_found():
    """
    Test retrieving a non-existent book.
    """
    client = APIClient()
    user = User.objects.create_superuser(username="admin", email="admin@example.com", password="adminpass")
    client.force_authenticate(user=user)

    response = client.get("/api/books/999/")
    
    assert response.status_code == 404
