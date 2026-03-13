from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Clerk', 'Clerk'),
        ('Driver', 'Driver'),
        ('Auditor', 'Auditor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Clerk')

    def __str__(self):
        return f"{self.username} ({self.role})"
