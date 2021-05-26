from typing import Text
from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField

# Create your models here.

class Skills(models.Model):
    title = CharField(max_length=30)
    per = IntegerField()


class Education_History(models.Model):
    name = CharField(max_length=60)
    place = CharField(max_length=60)
    text = TextField()
    startdate = CharField(max_length=13)
    enddate = CharField(max_length=13)


class Working_History(models.Model):
    name = CharField(max_length=60)
    place = CharField(max_length=60)
    text = TextField()
    startdate = CharField(max_length=13)
    enddate = CharField(max_length=13)