from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView
from django.core.paginator import Paginator
from .models import Post, Profile
from .forms import ProfileForm
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


def detail_profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'blog/profile-detail.html', context)


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'blog/profile-update.html'

    def get_success_url(self):
        return reverse_lazy('blog-profile-detail', kwargs={'id': self.object.id})
