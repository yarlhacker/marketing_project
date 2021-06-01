from django.contrib.auth.models import User
from django.db import models


class Base(models.Model):
    
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta :
        abstract  = True


class  Banner(Base):

    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    
class  About(Base):
    
    title = models.CharField(max_length=250)
    description =  models.TextField()
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

class  Temoingnage(Base):
    
    description = models.TextField()
    nom = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Temoingnage'
        verbose_name_plural = 'Temoingnages'

class  Website(Base):
    
    numero= models.CharField(max_length=250)
    nom_site= models.CharField(max_length=250)
    logo_site= models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    mapp = models.TextField()
    email= models.CharField(max_length=250)
    slogan = models.CharField(max_length=250)


    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'wensite'
        verbose_name_plural = 'wensites'



class  Configuration(Base):
    

    entete_service = models.TextField() 
    image_newsletter = models.FileField(upload_to='images')
    entete_newsletter = models.TextField() 
    entete_contact = models.TextField() 
    instruction_contact = models.TextField() 
    copyright = models.CharField(max_length=250)

    
    
    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'


class  Sociaux(Base):
    
    nom = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    lien = models.URLField(max_length=200)

    def __str__(self):
        return self.nom 
        
    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'Sociaux'


class Profil(Base):
    user = models.OneToOneField(User, related_name="profil_user", on_delete=models.CASCADE)
    image= models.FileField(upload_to='images')
    profession = models.CharField(max_length=250)
