from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "description": "Это домашняя страница сайта - Home!",
    }
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")
