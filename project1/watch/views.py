from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request, 'watch/index.html')

def home(request):
    images = Brand.objects.all()
    return render(request, 'watch/home.html',{'brand_images':images})

def product(request):
    products = Products.objects.all()
    return render(request,'watch/product.html', {'products': products})

def catalog(request):
    products = Products.objects.all()
    return render(request, 'watch/catalog.html',{'products':products})
def servises(request):
    return render(request,'watch/servises.html')

def about(request):
    return render(request,'watch/about.html')

def contact(request):
    return render(request,'watch/contact.html')

def login(request):
    images=Brand.objects.all()
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customer = Customer.objects.get(email=email, password=password)
            return render(request, 'watch/home.html', {'customer': customer, 'brand_images':images} ) 
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

def trendy(request):
    products = Products.objects.filter(style='trendy')
    return render(request, 'watch/trendy.html', {'products': products})

def professional(request):
    products = Products.objects.filter(style='professional')
    return render(request, 'watch/profe.html', {'products': products})

def elegant(request):
    products = Products.objects.filter(style='elegant')
    return render(request, 'watch/elegant.html', {'products': products})

def luxuary(request):
    products = Products.objects.filter(style='Luxury')
    return render(request, 'watch/luxuary.html', {'products': products})

def sports(request):
    products = Products.objects.filter(style='sports')
    return render(request, 'watch/sport.html', {'products': products})

def smart(request):
    products = Products.objects.filter(style='smart')
    return render(request, 'watch/smart.html', {'products': products})

def size(request):
    return render(request, 'watch/size.html')

def ladies(request):
    products = Products.objects.filter(category='ladies')
    return render(request, 'watch/ladies.html', {'products': products})

def mens(request):
    products = Products.objects.filter(category='mens')
    return render(request, 'watch/mens.html', {'products': products})


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

