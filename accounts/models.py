from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Normal User'),
        ('expert', 'Tech Expert'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    country = models.CharField(max_length=50, default='Ghana')


@property
def is_expert(self):
    return self.role == 'expert'


class ExpertProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    verified = models.BooleanField(default=False)
    badge = models.CharField(max_length=50, default='Tech Expert')
