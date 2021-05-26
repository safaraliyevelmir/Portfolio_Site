from blog.models import Blog
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import Blog, Comment
from blog import models


@admin.register(Blog)
class Blog_Admin(admin.ModelAdmin):
    list_display = ['title','date']
    
    class Meta:
        model = Blog


@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    
    class Meta:
        model = Comment


