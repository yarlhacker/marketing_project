from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('images_view','title','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('images_view','title','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
  
@admin.register(models.Temoingnage)
class TemoingnageAdmin(admin.ModelAdmin):
    list_display = ('images_view','nom','profession','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
    

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('nom_site','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    

@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('images_view','copyright','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image_newsletter.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
    

@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    list_display = ('nom','lien','icon','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    

@admin.register(models.Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('images_view','profession','date_add','date_update','status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Apercu des images'
  