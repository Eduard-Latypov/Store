from django.shortcuts import render
from .models import Categories


def catalog(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "goods/catalog.html", context=context)


def product(request):
    return render(request, "goods/product.html")
