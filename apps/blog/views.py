from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Profile, CategoryPost
from .forms import ProfileForm, CommentForm, FilterForm, CreatePostForm, UpdatePostForm

from datetime import timedelta, datetime
from django.utils.timezone import make_aware

from django.db.models import Q


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.mixins import LoginRequiredMixin


from rest_framework import generics, status
from .serializers import PostSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response


class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-upload_date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm()

        return context


class FilterPostList(ListView):
    model = Post
    template_name = 'blog/post-search.html'
    ordering = ['-upload_date']
    paginate_by = 5

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
            from_upload_date = make_aware(
                datetime.strptime('1900-01-01', '%Y-%m-%d'))
        to_upload_date = self.request.GET.get(
            'to_upload_date')
        if to_upload_date:
            to_upload_date += " 23:59:59"

        object_list = Post.objects.filter(
            (Q(title__icontains=content) | Q(body__icontains=content))
            & Q(upload_date__range=(from_upload_date, to_upload_date))
        )

        if category:
            object_list = object_list.filter(Q(category=category))

        if author:
            object_list = object_list.filter(Q(author__username=author))
        return object_list.order_by('-upload_date')


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
        context = {'post': post, 'form': form}
        return render(request, 'blog/post-detail.html', context)


def create_profile(request):
    profile = Profile(user=request.user)
    profile.save()
    return redirect('blog-profile-detail', profile.id)


def detail_profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'blog/profile-detail.html', context)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Profile
    form_class = ProfileForm
    template_name = 'blog/profile-update.html'

    def get_success_url(self):
        return reverse_lazy('blog-profile-detail', kwargs={'id': self.object.id})


@method_decorator(staff_member_required(login_url='/login/'), name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/post-update.html'

    def get_success_url(self):
        return reverse_lazy('blog-post-detail', kwargs={'id': self.object.id})


def update_post(request, id):
    post = Post.objects.get(id=id)
    incoming_form = UpdatePostForm(
        request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST":
        if incoming_form.is_valid():
            incoming_form.save()
            return redirect(request.path)
    else:
        context = {'form': incoming_form}
        return render(request, 'blog/post-update.html', context)


@staff_member_required(login_url='/login/')
def create_post(request):
    if request.method == "POST":
        incoming_form = CreatePostForm(
            request.POST or None, request.FILES or None)
        if incoming_form.is_valid():
            post = incoming_form.save(commit=False)
            post.author = request.user
            post.save()

            # return redirect(request.path)
            return redirect('blog-post-detail', post.id)
    else:
        form = CreatePostForm()
        context = {'form': form}
        return render(request, 'blog/post-create.html', context)


@method_decorator(staff_member_required(login_url='/login/'), name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post-delete.html'
    success_url = reverse_lazy('blog-home')


class API_Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class API_Post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def API_Profiles(request):
    if request.method == "GET":
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def API_Profile_detail(request, pk):
    profile = get_object_or_404(Profile, id=pk)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
