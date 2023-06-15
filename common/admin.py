from django.contrib import admin
from .models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    # prepopulated_fields = {"slug": ("name",)}

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    # prepopulated_fields = {"slug": ("name",)}