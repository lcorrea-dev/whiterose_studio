from django.test import TestCase
from apps.blog.models import Post

from datetime import datetime
from django.utils.timezone import make_aware

from django.contrib.auth import get_user_model


class CommentTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create()
        body = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Praesent elementum vestibulum aliquam. In quis eleifend nisi. Ut pretium lorem ac magna orci. '''
        Post.objects.create(
            title='post20061025', upload_date=make_aware(datetime.strptime('2006-10-25', '%Y-%m-%d')), author=user, body=body+"1")
        Post.objects.create(
            title='post20101025', upload_date=make_aware(datetime.strptime('2010-10-25', '%Y-%m-%d')), author=user, body=body+"2")

    def test_create_post(self):
        body = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Praesent elementum vestibulum aliquam. In quis eleifend nisi. Ut pretium lorem ac magna orci. '''
        post1 = Post.objects.get(upload_date=make_aware(
            datetime.strptime('2006-10-25', '%Y-%m-%d')))
        post2 = Post.objects.get(upload_date=make_aware(
            datetime.strptime('2010-10-25', '%Y-%m-%d')))

        self.assertEqual(post1.title, 'post20061025')
        self.assertEqual(post2.title, 'post20101025')
