from django.urls import path
from .views import PostList, detail_post, detail_profile, ProfileUpdate

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('post/<int:id>', detail_post, name='blog-post-detail'),
    path('profile/<int:id>', detail_profile, name='blog-profile-detail'),
    path('profile/update/<int:pk>', ProfileUpdate.as_view(),
         name='blog-profile-update'),

]
