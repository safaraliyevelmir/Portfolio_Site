from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField, EmailField, SlugField, TextField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
import datetime


def gen_slug(slug):
    return slugify(slug,allow_unicode=False) 


# Create your models here.

class Blog(models.Model):
    title = CharField(max_length=30)
    slug = SlugField(max_length=50, null=True, blank=True)
    img = ImageField(upload_to='images')
    text = RichTextField()
    date = DateField(auto_now_add=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)

        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse("single_blog", kwargs={"slug": self.slug})
    





class Comment(models.Model):
    datetime = DateTimeField(auto_now_add=True)
    name = CharField(max_length=50)
    email = EmailField(max_length=70)
    message = TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_comment')