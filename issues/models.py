from django.db import models
from accounts.models import User


class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='issues/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
