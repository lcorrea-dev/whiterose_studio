from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)
    upload_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover = models.ImageField()


def __str__(self):
    return self.title
