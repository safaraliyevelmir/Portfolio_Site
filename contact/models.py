from django.db import models
from django.db.models.fields import TextField
from django.forms.fields import CharField, EmailField

# Create your models here.

class Contact(models.Model):
    name = CharField(max_length=50)
    email = EmailField(max_length=50)
    subject = CharField(max_length=60)
    text = TextField()


