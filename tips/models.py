from django.db import models

class TechTip(models.Model):
    expert = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='tips/', null=True, blank=True)
