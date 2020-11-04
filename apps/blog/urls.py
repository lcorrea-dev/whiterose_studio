from django.urls import path
from .views import Home, detail_post

urlpatterns = [
    path('', Home.as_view(), name='blog-home'),
    path('post/<int:id>', detail_post, name='blog-post-detail'),
]
