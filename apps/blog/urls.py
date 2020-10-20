from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('gallery/', views.gallery, name='blog-gallery'),
]
