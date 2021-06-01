from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('blog/', views.blog , name = 'blog'),
    path('detail_blog/', views.detail_blog , name = 'detail_blog'),
    path('contact/', views.contact, name = 'contact'),
    path('detail_project/<int:id>/', views.detail_project, name = 'detail_project')
]