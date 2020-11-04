from django.urls import path
from .views import home, detail_post

urlpatterns = [
    path('', home, name='blog-home'),
    path('post/<int:id>', detail_post, name='blog-post-detail'),
]
