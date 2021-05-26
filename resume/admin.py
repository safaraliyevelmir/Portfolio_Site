from django.contrib import admin
from django.db import models

from .models import Education_History, Working_History, Skills

# Register your models here.

@admin.register(Skills)
class Skill_Admin(admin.ModelAdmin):

    list_display = ['title','per']

    class Meta:
        model =  Skills

@admin.register(Education_History)
class Education_Admin(admin.ModelAdmin):

    list_display = ['name','place']

    class Meta:
        model =Education_History


@admin.register(Working_History)
class Work_Admin(admin.ModelAdmin):
    
    list_display = ['place','name']
    
    class Meta:
        model = Working_History
