from django.contrib import admin

from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    fieldsets = (
        (None, {"fields": (
            "title", "slug", "content", "photo", "time_create", "time_update", "is_published", "department", "author"
        )}),
    )
    readonly_fields = ["time_create", "time_update"]

    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

