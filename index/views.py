from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "home_page":"active"
    }
    return render(request,'index.html', context)