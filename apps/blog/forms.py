from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Profile, Comment, CategoryPost, Post

from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.utils import timezone


class ProfileForm(UserChangeForm):
    password = None

    class Meta:

        model = Profile
        fields = [

            'pic',
            'website_url',
            'fb_url',
            'twitter_url',
            'instagram_url',
            'bio',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {
            'body': forms.Textarea(), }
        labels = {
            'body': "Write your comment here",
        }


class FilterForm(forms.Form):
    content = forms.CharField(label='Content text',
                              max_length=50, required=False)
    category = forms.ModelChoiceField(label='Category',
                                      queryset=CategoryPost.objects.all(), empty_label="All", required=False)
    author = forms.CharField(label='Author', max_length=50, required=False)
    from_upload_date = forms.DateField(
        label='From', required=False, widget=AdminDateWidget())
    to_upload_date = forms.DateField(label='To',
                                     required=False, initial=timezone.now, widget=AdminDateWidget())


class CreatePostForm(forms.ModelForm):
    upload_date = forms.SplitDateTimeField(
        initial=timezone.now, widget=AdminSplitDateTime())

    class Meta:
        model = Post
        fields = ['title', 'category', 'upload_date', 'cover', 'body']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'cover', 'body', ]
