from django.db import models
from django.db.models.fields import CharField, DateField, DateTimeField, EmailField, SlugField, TextField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
import datetime

# Create your models here.



def gen_slug(slug):
    return slugify(slug,allow_unicode=False) 


class Portfolio(models.Model):
    title = CharField(max_length=60)
    subtitle = CharField(max_length=60)
    githiblink = CharField(max_length=400)
    slug = SlugField(max_length=50, null=True, blank=True)
    img = ImageField(upload_to='images')
    text = RichTextField()
    startdate = DateField(auto_now_add=True)
    enddate = DateField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)

        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse("portfolio_single", kwargs={"slug": self.slug})


class Comment(models.Model):
    datetime = DateTimeField(auto_now_add=True)
    name = CharField(max_length=50)
    email = EmailField(max_length=70)
    message = TextField()
    post = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolio_comment')
