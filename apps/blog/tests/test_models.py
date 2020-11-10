from django.test import TestCase
from ..models import Comment, Post
from ..forms import CommentForm
from django.contrib.auth import get_user_model


class CommentTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create()
        body = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Praesent elementum vestibulum aliquam. In quis eleifend nisi. Ut pretium lorem ac magna orci. '''
        Post.objects.create(
            title='post1', upload_date='2006-10-25', author=user, body=body+"1")
        Post.objects.create(
            title='post2', upload_date='2010-10-25', author=user, body=body+"2")

    def test_create_post(self):

        body = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Praesent elementum vestibulum aliquam. In quis eleifend nisi. Ut pretium lorem ac magna orci. '''
        post1 = Post.objects.get(title='post1')
        post2 = Post.objects.get(title='post2')

        self.assertEqual(post1.body, body+"1")
        self.assertEqual(post2.body, body+"2")

        self.assertEqual(post1.title, 'post1')
        self.assertEqual(post2.title, 'post2')
