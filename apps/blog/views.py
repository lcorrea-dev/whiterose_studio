from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView
from django.core.paginator import Paginator
from .models import Post, Profile, CategoryPost
from .forms import ProfileForm, CommentForm, FilterForm

from django.db.models import Q


class PostList(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enabled'] = True
        context['form'] = FilterForm()
        return context


class FilterPostList(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/post-search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enabled'] = True
        context['form'] = FilterForm()
        return context

    def get_queryset(self):
        content = self.request.GET.get('content')
        if not content:
            content = ""
        category = self.request.GET.get('category')
        author = self.request.GET.get('author')
        from_upload_date = self.request.GET.get('from_upload_date')
        if not from_upload_date:
            from_upload_date = '1900-01-01'
        to_upload_date = self.request.GET.get('to_upload_date')

        object_list = Post.objects.filter(
            (Q(title__icontains=content) | Q(body__icontains=content))
            & Q(upload_date__range=(from_upload_date, to_upload_date))
        )

        if category:
            object_list = object_list.filter(Q(category=category))

        if author:
            object_list = object_list.filter(Q(author__username=author))
        return object_list


def detail_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        incoming_form = CommentForm(request.POST)
        if incoming_form.is_valid():
            comment = incoming_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()
        # post = Post.objects.get(id=id)
        context = {'post': post, 'form': form}
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
