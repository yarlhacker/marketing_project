from django.contrib import admin
from . import models 


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

# Register your models here.
