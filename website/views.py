from django.shortcuts import render ,get_object_or_404
from . import models
from service import models as models_service



def index(request):
    banner = models.Banner.objects.filter(status=True).first()
    about  = models.About.objects.filter(status=True).first()
    services = models_service.Service.objects.filter(status=True)
    temoingnages = models.Temoingnage.objects.filter(status=True)

    return render(request, 'index.html',locals())


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')

def detail_blog(request):
    return render(request, 'blog-detail.html')

def detail_project(request , id):

    service = get_object_or_404(models_service.Service , id=id )
    return render(request, 'project-detail.html',locals())

# Create your views here.
