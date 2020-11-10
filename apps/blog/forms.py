from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Profile, Comment, CategoryPost, Post

from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone


class ProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'pic',
            'website_url',
            'fb_url',
            'twitter_url',
            'instagram_url',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}), }


class FilterForm(forms.Form):
    content = forms.CharField(label='Content text',
                              max_length=50, required=False)
    category = forms.ModelChoiceField(label='Category',
                                      queryset=CategoryPost.objects.all(), empty_label="All", required=False)
    author = forms.CharField(label='Author', max_length=50, required=False)
    from_upload_date = forms.DateField(
        label='date', required=False, widget=AdminDateWidget())
    to_upload_date = forms.DateField(
        required=False, initial=timezone.now, widget=AdminDateWidget())
