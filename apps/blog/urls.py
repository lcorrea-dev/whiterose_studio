from django.urls import path
from .views import PostList, detail_post, detail_profile, ProfileUpdate, FilterPostList, create_post, PostDelete, PostUpdate, update_post

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('post/<int:id>', detail_post, name='blog-post-detail'),
    path('post/search/', FilterPostList.as_view(), name='blog-post-search'),
    path('post/create/', create_post, name='blog-post-create'),
    path('profile/<int:id>', detail_profile, name='blog-profile-detail'),
    path('profile/update/<int:pk>', ProfileUpdate.as_view(),
         name='blog-profile-update'),
    path('post/delete/<int:pk>', PostDelete.as_view(),
         name='blog-post-delete'),
    path('post/update/<int:pk>', PostUpdate.as_view(),
         name='blog-post-update'),

]
