from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=60)
    message = forms.CharField(widget=Textarea)