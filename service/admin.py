from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title','date_add','date_update','status',)
    date_hierarchy = 'date_add'
    list_editable = ['status']



@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('images_view','images_view1','title', 'categorie','date_add','date_update','status',)
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
    
    def images_view1(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view1.short_description = 'Apercu des images'


@admin.register(models.Categorieblog)
class CategorieblogAdmin(admin.ModelAdmin):
    list_display = ('title','date_add','date_update','status',)
    date_hierarchy = 'date_add'
    list_editable = ['status']


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('images_view','title','date_add','date_update','status',)
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
 
@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status',)
    date_hierarchy = 'date_add'
    list_editable = ['status']

# Register your models here.
