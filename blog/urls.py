from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
    
    
]
