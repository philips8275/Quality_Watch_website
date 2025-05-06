from django.shortcuts import render
from .models import Customer
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

def login(request):
    return render(request, 'watch/login.html')

def signup(request):
    return render(request, 'watch/signup.html')

def submit_register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword =request.POST.get("confirmpassword")
        phone=request.POST.get("phone")
        address=request.POST.get("address")

        customer = Customer(
            name = name,
            email =email,
            password=password,
            confirmpassword=confirmpassword,
            phone=phone,
            address=address

        )
        try:
            customer.save()
            return render(request,'watch/home.html')
        except:
            return render(request,'watch/home.html')
    return render(request,'watch/home.html')

    