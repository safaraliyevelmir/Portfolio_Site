from typing import Text

from django.forms import forms
from .models import Contact
from contact.forms import ContactForm
from django.shortcuts import redirect, render

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        contactform = Contact()
        contactform.save()
    
    context = {
        'contact_page':'active',
        'form':form
    }
    return render(request, 'contacts.html', context)