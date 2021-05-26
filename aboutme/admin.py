from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Cv,Image, Main_Info, Other_Info, Services
from aboutme import models

# Register your models here.

@admin.register(Other_Info)
class Aboutme_Admin(admin.ModelAdmin):
    
    list_display = ['title', 'info']

    class Meta:
        model= Other_Info


@admin.register(Main_Info)
class Other_Info_Admin(admin.ModelAdmin):

    list_display=['name','information']

    class Meta:
        model = Main_Info

@admin.register(Services)
class Services_Admin(admin.ModelAdmin):

    list_display=['title']

    class Meta:
        model = Services


admin.site.register(Cv)
admin.site.register(Image)

