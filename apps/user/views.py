from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm

# Create your views here.


class RegisterUser(CreateView):
    model = User
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('list_user')


class UserList(ListView):
    model = User
    template_name = 'user/list.html'
