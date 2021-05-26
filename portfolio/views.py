from django.shortcuts import render

# Create your views here.

def portfolio(request):
    context = {
        'portfolio_page':'active'
    }
    return render(request, 'portfolio.html', context)