from django.shortcuts import render, redirect
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


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update_template.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('post_list_url')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete_template.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list_url')


def FlowersView(request):
    color = request.GET.get('color')
    if color is not None:
        flowers_all = Flower.objects.filter(color=color.capitalize())
    else:
        flowers_all = Flower.objects.all()
    context = {
        'flowers': flowers_all,
        'message': 'Hello my Friend! :)'
    }
    return render(request=request, template_name='flowers_template.html', context=context)


def FlowersDetailView(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    context = {
        'flower': flower
    }
    return render(request=request, template_name='flower_detail_template.html', context=context)


def FlowerCreateView(request):
    if request.method == 'GET':
        return render(request=request, template_name='flower_create_template.html')
    elif request.method == 'POST':
        name = request.POST.get('name').capitalize()
        color = request.POST.get('color').capitalize()
        image = request.FILES.get('image')
        flower = Flower(name=name, color=color, image=image)
        flower.save()
        return redirect('flowers_url')
