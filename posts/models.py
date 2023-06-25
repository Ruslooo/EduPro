from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from pytils.translit import translify

from common.models import *
from profiles.models import *


class Post(models.Model):
    VISIBLE_TO_CHOICES = (
        ('all', 'Всем'),
        ('department', 'Кафедре'),
    )
    title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст поста')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, verbose_name='Автор')
    department = models.ForeignKey('common.Department', on_delete=models.CASCADE, verbose_name='Кафедра')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    likes = models.ManyToManyField('profiles.Profile', related_name='blogpost_like')

    visible_to = models.CharField(max_length=20, choices=VISIBLE_TO_CHOICES, default='all',
                                  verbose_name='Видимость поста')

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        return self.likes.all().count()

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"post_slug": self.slug or self.title})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']

    def save(self, *args, **kwargs):
        slug = slugify(translify(self.title))

        if Post.objects.filter(slug__exact=slug).exists():
            self.slug = slug + get_random_string(3)
        else:
            self.slug = slug

        super().save(*args, **kwargs)


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)