from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd["username"], password=cd["password"])
            if user and user.is_active:
                auth.login(request, user)
                return redirect(reverse("main:index"))
    else:
        form = UserLoginForm()
    context = {"title": "Home - Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("user:login"))
    else:
        form = UserRegisterForm()
    context = {"title": "Home - Регистрация", "form": form}
    return render(request, "users/register.html", context)


def profile(request):
    context = {"title": "Home - Профиль"}
    return render(request, "users/profile.html", context)


def logout(request):
    pass
