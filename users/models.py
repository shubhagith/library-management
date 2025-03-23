from django.contrib.auth.models import User
from django.db import models

class AdminProfile(models.Model):
    """Extends Django's default User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_library_admin = models.BooleanField(default=True)  # Flag to identify admins

    def __str__(self):
        return self.user.email
