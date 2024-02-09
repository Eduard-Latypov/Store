from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Categories, Products
from .utils import q_search


def catalog(request, slug):
    queryset = Products.objects.select_related("category")
    if slug == "vse-tovary":
        goods = queryset
    else:
        goods = get_list_or_404(queryset, category__slug=slug)

    query = request.GET.get("q", None)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    if query:
        goods = q_search(query)
    if on_sale:
        goods.filter(discount__gt=0)
    if order_by:
        goods.order_by(order_by)

    category = goods[0].category
    paginator = Paginator(goods, 3)
    page_num = request.GET.get("page", 1)
    current_page = paginator.get_page(page_num)
    context = {
        "goods": current_page,
        "category": category,
        "title": "Home - Каталог",
    }
    return render(request, "goods/catalog.html", context=context)


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {"product": product}
    return render(request, "goods/product.html", context=context)
