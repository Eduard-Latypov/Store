from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")
