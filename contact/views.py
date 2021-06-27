from blog.forms import CommentForms
from typing import Text

from django.forms import forms
from .models import Contact
from contact.forms import ContactForm
from django.shortcuts import redirect, render

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form = Contact(name=name,email=email,subject=subject,text=message)
            form.save()
            return redirect('index')
        
        else:
            form = CommentForms()

    context = {
        'contact_page':'active',
        'form':form
    }
    return render(request, 'contacts.html', context)