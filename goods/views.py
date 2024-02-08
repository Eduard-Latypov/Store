from django.shortcuts import render
from .models import Categories, Products


def catalog(request):
    products = Products.objects.all()
    context = {"categories": products}
    return render(request, "goods/catalog.html", context=context)


def product(request):
    return render(request, "goods/product.html")
