from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import Textarea

class CommentForms(forms.Form):
    name = CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Your Name *'}))
    email = EmailField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Your Email *'}))
    comment = CharField(widget=Textarea(attrs={'placeholder':'Your Message *'}), max_length=500)