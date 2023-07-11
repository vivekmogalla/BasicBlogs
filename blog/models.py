from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title