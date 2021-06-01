from django.contrib import admin
from . import models 


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','created_at','updated_at','status')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','created_at','updated_at','status')

# Register your models here.
