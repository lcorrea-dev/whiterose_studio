from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)
    upload_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover = models.ImageField()
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(
        'CategoryPost', on_delete=models.CASCADE, blank=True, null=True,
    )

    def __str__(self):
        return self.title


class CategoryPost(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, related_name='replies', on_delete=models.CASCADE, blank=True)
    body = models.TextField(max_length=500)
    upload_date = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.author) + self.body
