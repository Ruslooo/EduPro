from django.db import models
from profiles.models import *
from posts.models import *

class Comment(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField()
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, verbose_name='Пост')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content