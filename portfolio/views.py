from blog.forms import CommentForms
from django.core import paginator
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Portfolio, Comment
from django.urls import reverse

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all()
    paginator = Paginator(portfolios,6)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context = {
        'portfolio_page':'active',
        'page_obj':page_obj
    }
    return render(request, 'portfolio.html', context)


def portfolio_single(request,slug):
    portfolio = Portfolio.objects.get(slug=slug)
    form = CommentForms(request.POST or None)
    comment = Comment.objects.filter(id=portfolio.id).all()
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            post_id = portfolio.id
            form = Comment(name=name,email=email,message=comment, post_id=post_id)
            form.save()
            return redirect(reverse('portfolio_single',args=[slug]))
        
        else:
            form = CommentForms()

    context = {
        'portfolio_page':'active',
        'portfolio':portfolio,
        'form':form,
        'comment':comment
    }
    return render(request, 'portfoliosingle.html', context)