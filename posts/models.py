from django.db import models
from accounts.models import User

class Post(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    file = models.FileField(upload_to='posts/files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
