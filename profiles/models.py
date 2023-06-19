from django.contrib.auth.models import AbstractUser, UserManager
from common.models import *

class Profile(AbstractUser, UserManager):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default="avatars_default/avatar.png", verbose_name='Фото')
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    institute = models.ForeignKey('common.Institute', on_delete=models.SET_NULL, null=True, verbose_name='Институт')
    department = models.ForeignKey('common.Department', on_delete=models.SET_NULL, null=True, verbose_name='Кафедра')

    def __str__(self):
        return self.username