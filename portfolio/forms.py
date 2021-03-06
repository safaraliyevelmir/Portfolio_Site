from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import TextInput, Textarea

class CommentForms(forms.Form):
    name = CharField(max_length=30)
    email = EmailField(max_length=50)
    comment = CharField(widget=Textarea, max_length=500)