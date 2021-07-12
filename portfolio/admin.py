from django.contrib import admin

# Register your models here.

from .models import Portfolio, Comment

admin.site.register(Portfolio)
admin.site.register(Comment)