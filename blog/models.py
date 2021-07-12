from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField, EmailField, SlugField, TextField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
import datetime




# Create your models here.

class Blog(models.Model):
    title = CharField(max_length=30)
    slug = CharField(max_length=300)
    img = ImageField(upload_to='images')
    date = DateField(auto_now_add=True)



class Comment(models.Model):
    datetime = DateTimeField(auto_now_add=True)
    name = CharField(max_length=50)
    email = EmailField(max_length=70)
    message = TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_comment')