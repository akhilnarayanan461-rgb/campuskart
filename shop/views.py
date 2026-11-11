from django.shortcuts import render
from . models import Product

def home(request):
    products=Product.objects.all()
    return render(request,"shop/home.html",{"products":products})
def about(request):
    return render(request,"shop/about.html")
def product_deatils(request,id):
    product=Product.objects.get(id=id)
    return render (request,"shop/product_deatils.html",{"product":product})
def cheap_products(request):
    product=Product.objects.filter(price__lt=30)
    return render (request,"shop/cheap_products.html")