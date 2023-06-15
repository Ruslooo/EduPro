from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from pytils.translit import translify

from profiles.models import *
from common.models import *

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст поста')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    author = models.ForeignKey('profiles.Profile', on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Автор')
    department = models.ForeignKey('common.Department', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Кафедра')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']

    def save(self, *args, **kwargs):
        slug = slugify(translify(self.title))

        if Post.objects.filter(slug__exact=slug).exists():
            self.slug = slug + get_random_string(3)

        super().save(*args, **kwargs)



    VISIBLE_TO_CHOICES = (
        ('all', 'Всем'),
        ('department', 'Кафедре'),
    )

    visible_to = models.CharField(max_length=20, choices=VISIBLE_TO_CHOICES, default='all',
                                  verbose_name='Видимость поста')