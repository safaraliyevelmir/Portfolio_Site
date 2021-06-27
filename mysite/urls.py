"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from contact.views import contact
from django.contrib import admin
from django.urls import path

from index.views import index
from aboutme.views import aboutme
from blog.views import blog,single_blog
from contact.views import contact
from portfolio.views import portfolio, portfolio_single
from resume.views import resume


from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('resume/', resume, name='resume'),
    path('blog/', blog, name='blog'),
    path('about/',aboutme, name='about'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('singleblog/<slug:slug>/',single_blog, name='single_blog'),
    path('portfolio/<slug>/',portfolio_single, name='portfolio_single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


