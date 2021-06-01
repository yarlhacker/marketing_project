from django.contrib import admin
from . import models


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at','status',)



@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie','created_at','updated_at','status',)


@admin.register(models.Categorieblog)
class CategorieblogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at','status',)



@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at','status',)


@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom','created_at','updated_at','status',)









# Register your models here.
