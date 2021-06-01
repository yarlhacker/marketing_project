from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import FileField
from website.models import Base

class  Categorie(Base):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'


class  Service(Base):
    title = models.CharField(max_length=250)
    logo = models.FileField(upload_to='images')
    introduction = models.TextField()
    nom = models.CharField(max_length=250)
    nom_compagny = models.CharField(max_length=250)
    title_soustitre = models.CharField(max_length=250)
    image = models.FileField(upload_to='images')
    image_pricipal = models.FileField(upload_to='images')
    video = models.URLField(max_length=255)
    conclusion = models.TextField()
    categorie = models.ForeignKey("service.Categorie",related_name = 'categorieservice' ,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'


class  Categorieblog(Base):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'categorieblog'
        verbose_name_plural = 'categorieblogs'


class Blog(Base):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='images')
    description = models.TextField()
    auteur = models.ForeignKey(User, related_name='auteur_blog', on_delete=models.CASCADE)
    categorie = models.ForeignKey("service.Categorieblog",related_name = 'categorieblog' ,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Commentaire(Base):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'



