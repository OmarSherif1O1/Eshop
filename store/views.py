from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, id):
    products = product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'products': products})

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')