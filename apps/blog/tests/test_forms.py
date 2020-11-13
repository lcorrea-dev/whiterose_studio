from django.test import TestCase
from apps.blog.forms import CommentForm


class CommentFormCase(TestCase):
    def test_valid_form(self):
        data = {'body': 'lorem ipsum'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'body': ''}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
