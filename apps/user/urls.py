from django.urls import path, include
from . import views
from .views import RegisterUser, UserList

urlpatterns = [
    path('register', RegisterUser.as_view(), name="register_user"),
    path('list', UserList.as_view(), name="list_user"),
]
