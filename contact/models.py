from django.db import models
from website.models import Base

class  Newsletter(Base):
    
    email = models.URLField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class  Contact(Base):
    nom = models.CharField(max_length=50)
    email = models.URLField(max_length=200)
    meassage = models.TextField()

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

# Create your models here.
