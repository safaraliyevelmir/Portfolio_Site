from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField, ImageField

# Create your models here.


class Image(models.Model):
    img = ImageField(upload_to='images')



class Cv(models.Model):
    cv = FileField()


class Main_Info(models.Model):
    name = CharField(max_length=30)
    information = CharField(max_length=300)

    def __str__(self):
        return self.name


class Other_Info(models.Model):
    title = CharField(max_length=30)
    info = CharField(max_length=30)

    def __str__(self):
        return self.title


class Services(models.Model):
    icon = CharField(max_length=50)
    title = CharField(max_length=50)
    subtitle = CharField(max_length=300)