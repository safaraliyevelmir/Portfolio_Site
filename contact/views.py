from .forms import ContactForm
from typing import Text

from django.forms import forms
from .models import Contact
from contact.forms import ContactForm
from django.shortcuts import redirect, render

# Create your views here.

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

    context = {
        'contact_page':'active',
        'form':form
    }
    return render(request, 'contacts.html', context)