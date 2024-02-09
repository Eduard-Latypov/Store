from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Categories, Products


def catalog(request, slug):
    queryset = Products.objects.select_related("category")
    if slug == "vse-tovary":
        goods = queryset
    else:
        goods = get_list_or_404(queryset, category__slug=slug)
    context = {"goods": goods}
    return render(request, "goods/catalog.html", context=context)


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {"product": product}
    return render(request, "goods/product.html", context=context)
