from django.test import TestCase
from ..models import Comment, Post
from ..forms import CommentForm
from django.contrib.auth import get_user_model


class CommentTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create()
        post = Post.objects.create(title='post1', upload_date='2006-10-25', )
