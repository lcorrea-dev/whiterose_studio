from django.urls import path, include
from . import views
from .views import RegisterUser, UserList
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register_user"),
    path('list/', UserList.as_view(), name="list_user"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password-reset.html'),
         name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password-reset-done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password-reset-confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password-reset-complete.html'),
         name='password_reset_complete'),
]
