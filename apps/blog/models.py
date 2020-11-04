from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)
    upload_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover = models.ImageField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
