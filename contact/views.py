from django.shortcuts import render

# Create your views here.

def contact(request):
    context = {
        'contact_page':'active'
    }
    return render(request, 'contacts.html', context)