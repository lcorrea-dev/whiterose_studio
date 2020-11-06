from django.contrib.auth.forms import UserChangeForm
from .models import Profile


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
