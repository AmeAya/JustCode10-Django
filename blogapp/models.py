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


class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.color)
