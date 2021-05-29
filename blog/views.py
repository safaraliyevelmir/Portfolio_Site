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
    form = Comment_Add(request.POST)
    print("Postun idsi: ",blogs.slug)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            comment = Comment(name=name,email=email, message=message)
            comment.save()
            return redirect('blog')
    
    form = Comment_Add()

    context = {
        'blog_page': 'active',
        'blogs':blogs,
        'form':form
    }
    return render(request,'singleblog.html',context)    


