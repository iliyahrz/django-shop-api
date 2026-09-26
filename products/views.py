from django.shortcuts import render
from .models import Product

def shop(r):
    hameye_mahsoolat = Product.objects.all()
    return render(r, "products/shop.html", {'products': hameye_mahsoolat})

def product_detail(r, pk):
    mahsool = Product.objects.get(pk=pk)
    return render(r, "products/product.html", {'product':mahsool})