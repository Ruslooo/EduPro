from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from pytils.translit import translify, slugify

from common.models import Institute, Department
from posts.models import Post


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not (model := get_user_model()).objects.filter(username="admin").exists():
            model.objects.create_superuser(username="admin", password="admin")

        institute_names = ["Институт математического моделирования и игропрактики"]

        institutes_to_create = [
            Institute(title=title)
            for title in institute_names
        ]

        for institute in institutes_to_create:
            institute.save()

        department_names = ["Прикладная информатика в образовании"]
        categories_to_create = [
            Department(title=title, institute_id=1)
            for title in department_names
        ]

        for category in categories_to_create:
            category.save()

        posts_to_create = [
            Post(title=(name := "Пост#%d" % i), slug=translify(slugify(name)), department_id=1, author_id=1)
            for i in range(10)
        ]
        for post in posts_to_create:
            post.save()
