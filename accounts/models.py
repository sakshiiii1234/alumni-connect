from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('SENIOR', 'Senior'),
        ('JUNIOR', 'Junior'),
        ('TEACHER', 'Teacher'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username
