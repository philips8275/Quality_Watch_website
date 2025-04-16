from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'watch/index.html')

def home(request):
    return render(request, 'watch/home.html')

def product(request):
    return render(request,'watch/product.html')

def servises(request):
    return render(request,'watch/servises.html')


def about(request):
    return render(request,'watch/about.html')

def contact(request):
    return render(request,'watch/contact.html')