from django.shortcuts import render
from .models import Product

def shop(r):
    hameye_mahsoolat = Product.objects.all()
    return render(r, "products/shop.html", {'products': hameye_mahsoolat})

def product(r, item):
    mahsool = Product.objects.get(slug=item)
    return render(r, "products/product.html")