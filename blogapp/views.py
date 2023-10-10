from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'  # Под каким именем данные будут отзыватся в html
    template_name = 'post_list_template.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail_template.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create_template.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('post_list_url')
