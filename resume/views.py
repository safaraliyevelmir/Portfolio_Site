from django.shortcuts import render

# Create your views here.

from .models import Education_History, Working_History,Skills


def resume(request):
    edu = Education_History.objects.all()
    work = Working_History.objects.all()
    skills = Skills.objects.all()
    context = {
        'skills': skills,
        'work': work,
        'edu': edu,
        'resume_page':'active'
    }
    return render(request, 'resume.html', context)