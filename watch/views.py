from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request, 'watch/index.html')

def home(request):
    return render(request, 'watch/home.html')

def product(request):
    products = Products.objects.all()
    return render(request,'watch/product.html', {'products': products})

def servises(request):
    return render(request,'watch/servises.html')

def about(request):
    return render(request,'watch/about.html')

def contact(request):
    return render(request,'watch/contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customer = Customer.objects.get(email=email, password=password)
            return render(request, 'watch/home.html', {'customer': customer}) 
        except Customer.DoesNotExist:
            return render(request, 'watch/login.html', {'error': 'Invalid credentials'})
    return render(request, 'watch/login.html')

def signup(request):
    return render(request, 'watch/signup.html')

def logout(request):
    request.session.flush()
    return redirect('home')

def kids(request):
    products = Products.objects.filter(category='Kids')
    return render(request, 'watch/kids.html', {'products': products})

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
            return render(request,'watch/login.html')
        except:
            return render(request,'watch/home.html')
    return render(request,'watch/home.html')

def submit_contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        contact = Contactus(
            name=name,
            email=email,
            message=message,
        )
        try:
            contact.save()
            return render(request,'watch/contact.html')
        except:
            return render(request,'watch/contact.html')
    return render(request, 'watch/contact.html')

def submit_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        stock = request.POST.get("stock")
        category = request.POST.get("category")
        brand = request.POST.get("brand")

        product = Products(
            name=name,
            price=price,
            description=description,
            image=image,
            stock=stock,
            category=category,
            brand=brand
        )
        try:
            product.save()
            return render(request, 'watch/product.html')
        except:
            return render(request, 'watch/product.html')
    return render(request, 'watch/product.html')

