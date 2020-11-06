from django.urls import path
from .views import Home, detail_post, detail_profile

urlpatterns = [
    path('', Home.as_view(), name='blog-home'),
    path('post/<int:id>', detail_post, name='blog-post-detail'),
    path('profile/<int:id>', detail_profile, name='blog-profile-detail'),

]
