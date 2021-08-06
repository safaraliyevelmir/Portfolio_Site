
from typing import NewType
from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Blog, Comment
from .forms import CommentForms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,6)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context = {
        'blog_page': 'active',
        'page_obj':page_obj
    }
    return render(request,'blog.html', context)

def single_blog(request, slug):
    blogs = Blog.objects.get(slug=slug)
    form = CommentForms(request.POST or None)
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            post_id = blogs.id
            form = Comment(name=name,email=email,message=comment, post_id=post_id)
            form.save()
            print(slug)
            return redirect(reverse('single_blog'))
        
        else:
            form = CommentForms()

    
    context = {
        'blog_page': 'active',
        'blogs':blogs,
        'form': form
    }
    return render(request,'singleblog.html',context)    


