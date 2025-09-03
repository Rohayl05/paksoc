# Django equivalent of your Java User entity
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    # Django automatically gives us: username, email, password, first_name, last_name
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # User roles - same as your Java enum
    class Role(models.TextChoices):
        USER = 'USER', 'User'
        ADMIN = 'ADMIN', 'Admin'
        ORGANIZER = 'ORGANIZER', 'Organizer'
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    
    # Override email to make it required and unique
    email = models.EmailField(unique=True)
    
    # Use email for login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
