from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm
from ..blog.models import Profile
# Create your views here.


class RegisterUser(CreateView):
    model = User
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('list_user')

    def form_valid(self, form):
        response = super(CreateView, self).form_valid(form)
        Profile.objects.create(user=self.object).save()
        return response


class UserList(ListView):
    model = User
    template_name = 'user/list.html'
