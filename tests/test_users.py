import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_signup():
    """
    Test user signup endpoint.
    """
    client = APIClient()
    response = client.post("/api/auth/signup/", {
        "username": "admin1",
        "email": "admin@example.com",
        "password": "adminpassword"
    })
    assert response.status_code == 201

@pytest.mark.django_db
def test_user_login():
    """
    Test user login endpoint.
    """
    client = APIClient()
    User.objects.create_user(username="admin1", email="admin@example.com", password="adminpassword")
    response = client.post("/api/auth/login/", {
        "email": "admin@example.com",
        "password": "adminpassword"
    })
    assert response.status_code == 200
    assert "token" in response.data
