from contact.views import contact
from django.contrib import admin


from .models import Contact

# Register your models here.


# @admin.register(Contacts)
# class Contacts_Admin(admin.ModelAdmin):
#     pass

admin.site.register(Contact)
