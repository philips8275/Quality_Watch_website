from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('index/',index,name='index'),
    path('product/',product,name='product'),
    path('product/<int:id>/',submit_product, name='submit_product'),
    path('servises/',servises,name='servises'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('kids/',kids,name='kids'),
    path('ladies/',ladies,name='ladies'),
    path('mens/',mens,name='mens'),
    path('trendy/',trendy,name='trendy'),
    path('size/',size,name='size'),
    path('professional/',professional,name='professional'),
    path('elegant/',elegant,name='elegant'),
    path('sports/',sports,name='sports'),
    path('smart/',smart,name='smart'),
    path('luxuary/',luxuary,name='luxuary'),
    path('catalog/',catalog,name='catalog'),
    path('signup/',signup,name='signup'),
    path('submit_register/',submit_register,name='submit_register'),
    path('submit_contact/',submit_contact,name='submit_contact'),
    
    
]