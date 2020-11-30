from django.urls import path
from .views import PostList, detail_post, detail_profile, ProfileUpdate, FilterPostList, create_post, PostDelete, PostUpdate, update_post, API_Posts, API_Post_detail, API_Profiles, API_Profile_detail

from rest_framework.urlpatterns import format_suffix_patterns

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
    path('api/posts/', API_Posts.as_view(), name='api-posts'),
    path('api/posts/<int:pk>/', API_Post_detail.as_view(), name='api-post-detail'),
    path('api/profiles/', API_Profiles, name='api-profiles'),
    path('api/profiles/<int:pk>/', API_Profile_detail,
         name='api-profile-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
