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
        flower_types = FlowerType.objects.all()
        context = {
            'flower_types': flower_types
        }
        return render(request=request, template_name='flower_create_template.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('name').capitalize()
        color = request.POST.get('color').capitalize()
        flower_type = FlowerType.objects.get(id=request.POST.get('flower_type'))
        image = request.FILES.get('image')
        flower = Flower(name=name, color=color, image=image, type=flower_type)
        flower.save()
        return redirect('flowers_url')


def FlowerUpdateView(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    if request.method == 'GET':
        context = {
            'flower': flower
        }
        return render(request=request, template_name='flower_update_template.html', context=context)
    elif request.method == 'POST':
        flower.name = request.POST.get('name').capitalize()
        flower.color = request.POST.get('color').capitalize()
        if 'image' in request.FILES:
            flower.image = request.FILES.get('image')
        flower.save()
        return redirect('flowers_url')


def BouquetsView(request):
    bouquets = Bouquet.objects.all()
    context = {
        'bouquets': bouquets
    }
    return render(request=request, template_name='bouquets_template.html', context=context)


def BouquetsDetailView(request, bouquet_id):
    bouquet = Bouquet.objects.get(id=bouquet_id)
    context = {
        'bouquet': bouquet
    }
    return render(request=request, template_name='bouquet_detail_template.html', context=context)


def BouquetsCreateView(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        context = {
            'flowers': flowers
        }
        return render(request=request, template_name='bouquet_create_template.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        flowers = request.POST.getlist('flowers')
        bouquet = Bouquet(name=name)
        bouquet.save()
        for flower in flowers:
            bouquet.flowers.add(Flower.objects.get(id=flower))
        bouquet.save()
        return redirect('bouquets_url')


def musicView(request):
    musics = Music.objects.all()
    context = {
        'musics': musics
    }
    return render(request=request, template_name='music_template.html', context=context)
