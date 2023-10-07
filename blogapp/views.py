from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class PostListView(ListView):
    model = Post
    template_name = 'post_list_template.html'
