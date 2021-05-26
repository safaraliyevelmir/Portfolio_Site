from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import Textarea

class Comment_Add(forms.Form):
    name = CharField(max_length=30)
    email = EmailField(max_length=50)
    comment = CharField(widget=Textarea, max_length=500)