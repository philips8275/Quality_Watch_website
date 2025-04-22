from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('home/',home,name='home'),
    path('product/',product,name='product'),
    path('servises/',servises,name='servises'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    
]