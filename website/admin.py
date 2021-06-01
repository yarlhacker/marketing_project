from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models



@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at','status')
    

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at','status')

@admin.register(models.Temoingnage)
class TemoingnageAdmin(admin.ModelAdmin):
    list_display = ('created_at','updated_at','status')


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('nom_site','created_at','updated_at','status')


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('created_at','updated_at','status')


@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    list_display = ('nom','created_at','updated_at','status')


@admin.register(models.Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'image', 'created_at','updated_at','status')

    def image_views(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:20px; height:100px">')

