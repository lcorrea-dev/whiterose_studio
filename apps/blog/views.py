from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def detail_post(request, id):
    post = Post.objects.get(id=id)

    context = {'post': post}

    return render(request, 'blog/post-detail.html', context)
