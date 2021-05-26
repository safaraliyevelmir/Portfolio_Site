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
    forms = Comment_Add(request.POST or None)
    if forms.is_valid():
        name =  forms.cleaned_data.get('name')
        email = forms.cleaned_data.get('email')
        message = forms.cleaned_data.get('message')

        message = Comment(name=name, email=email, message=message)

        message.save()
        return redirect('blog')

    blogs = Blog.objects.get(slug=slug)
    
    context = {
        'blog_page': 'active',
        'blogs':blogs,
        'forms':forms
    }
    return render(request,'singleblog.html',context)    
                                                    