from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE_CHOICES = (
    ('Super_Admin', 'Super_Admin'),
    ('Admin', 'Admin'),
    ('User', 'User')
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username