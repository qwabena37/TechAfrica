from django.db import models
from issues.models import Issue
from accounts.models import User


class Solution(models.Model):
    issue = models.ForeignKey(Issue, related_name='solutions', on_delete=models.CASCADE)
    expert = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='solutions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
