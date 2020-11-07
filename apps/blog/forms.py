from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Profile, Comment


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
