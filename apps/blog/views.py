from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


class Home(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enabled'] = True
        return context


def detail_post(request, id):
    post = Post.objects.get(id=id)

    context = {'post': post}

    return render(request, 'blog/post-detail.html', context)
