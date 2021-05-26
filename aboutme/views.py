from django.shortcuts import render

# Create your views here.
from .models import Other_Info, Main_Info, Image, Cv, Services


def aboutme(request):
    other_infos = Other_Info.objects.all()
    main_infos = Main_Info.objects.all()
    services = Services.objects.all()
    images = Image.objects.all()
    context = {
        'other_infos': other_infos,
        'main_infos': main_infos,
        'about_page':'active',
        'services': services,
        'images': images,
    }
    return render(request, 'aboutme.html', context)