from datetime import date
from typing import NewType
from django.http import request
from django.shortcuts import redirect, render

from .models import Blog, Comment
from .forms import Comment_Add
# Create your views here.



def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blog_page': 'active',
        'blogs':blogs
    }
    return render(request,'blog.html', context)

def single_blog(request, slug):
    blogs = Blog.objects.get(slug=slug)
    new_comment = None
    if request.method == 'POST':
        comment_form = Comment_Add(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
            return redirect('blog')
    
    comment_form = Comment_Add()

    context = {
        'blog_page': 'active',
        'blogs':blogs,
        'form': comment_form
    }
    return render(request,'singleblog.html',context)    


