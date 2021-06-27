from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Portfolio, Comment

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all()
    paginator = Paginator(portfolios,4)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context = {
        'portfolio_page':'active',
        'page_obj':page_obj
    }
    return render(request, 'portfolio.html', context)


def portfolio_single(request,slug):
    portfolio = Portfolio.objects.get(slug=slug)
    context = {
        'portfolio_page':'active',
        'portfolio':portfolio
    }
    return render(request, 'portfoliosingle.html', context)