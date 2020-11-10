from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)
    upload_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover = models.ImageField(
        blank=True, upload_to='cover')
    body = RichTextField(validators=[MinLengthValidator(150)])
    category = models.ForeignKey(
        'CategoryPost', on_delete=models.CASCADE, blank=True, null=True,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.cover:
            self.cover = 'cover/default-cover-img.gif'
            super(Post, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True, upload_to="profile/")
    website_url = models.URLField(max_length=255, null=True, blank=True)
    fb_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


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
