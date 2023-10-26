from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE - каскадное удаление(Если этот User удалится, то и данный пост тоже удалится)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True - При первом создании поста, выставляется текущая дата. Изменить ее нельзя

    def __str__(self):
        return str(self.title) + ' - ' + str(self.created_at)[:19]


class FlowerType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='flowers/', null=True, blank=True)
    type = models.ForeignKey('FlowerType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.color)


class Bouquet(models.Model):
    name = models.CharField(max_length=100)
    flowers = models.ManyToManyField('Flower')
    # ManyToMany по умолчанию может быть пустым, поэтому для него on_delete е требуется

    def __str__(self):
        return self.name


class Music(models.Model):
    music = models.FileField(upload_to='music/')
